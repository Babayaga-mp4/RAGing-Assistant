import argparse
import os
import sys
import uuid
from utils import TextUtils
from llm import ChatBot
from vectordb import VectorDBUtils
from redis_helper import redis_driver

os.environ["OPENAI_API_KEY"] = "sk-****" # Your OpenAI Key

def main(path):
    text_object = TextUtils()
    vector_object = VectorDBUtils()
    redis_object = redis_driver()

    extracted_text = text_object.extract_text(path)
    chunked_text = text_object.chunk_pdf(extracted_text)
    vector_fetch = vector_object.create_embeddings(chunked_text)

    conversation_key = str(uuid.uuid4())
    print(f"[{conversation_key}] Your document at {args.pdf_path} has been scanned successfully. Ask away!")
    
    while True:
        query = str(input("User: "))
        context = vector_fetch.similarity_search(query, k=1)
        chatbot = ChatBot()
        # response = chatbot.chatty_boi(result, query)
        history = redis_object.get_history(conversation_key)
        response = chatbot.chatty_boi(context, query, history)
        answer = ""
        for chunk in response:
            # if not chunk['done']: # Use along side ollama
            if chunk.choices[0].delta.content:
                # sys.stdout.write(chunk['message']['content'])
                sys.stdout.write(chunk.choices[0].delta.content)
                answer += chunk.choices[0].delta.content
                sys.stdout.flush()
        message_tuple = text_object.build_history(query, answer, context)
        redis_object.insert_history(conversation_key, message_tuple)
        print()


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Process a PDF and interact with a chatbot via CLI.")
    parser.add_argument("pdf_path", type=str, help="The path to the PDF file.")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"File not found: {args.pdf_path}")
        sys.exit(1)

    main(args.pdf_path)
    

# python main.py docs/NIPS-2017-attention-is-all-you-need-Paper.pdf