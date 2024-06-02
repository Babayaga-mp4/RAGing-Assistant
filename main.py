import argparse
import os
import sys
from utils import ChatBot, TextUtils, VectorDBUtils
os.environ["OPENAI_API_KEY"] = "sk-proj-TgfdYEYMUR2LGiu5frtcT3BlbkFJMDbYpPjLsPlpRkfM0dz5"

if __name__=="__main__":

    text_object = TextUtils()
    vector_object = VectorDBUtils()
    parser = argparse.ArgumentParser(description="Process a PDF and interact with a chatbot via CLI.")
    parser.add_argument("pdf_path", type=str, help="The path to the PDF file.")
    args = parser.parse_args()

    extracted_text = text_object.extract_text(args.pdf_path)

    chunked_text = text_object.chunk_pdf(extracted_text)
    vector_fetch = vector_object.create_embeddings(chunked_text)

    print(f"Your document at {args.pdf_path} has been scanned successfully. Ask away!")
    while True:
        query = str(input("User: "))
        result = vector_fetch.similarity_search(query, k=1)
        chatbot = ChatBot()
        # response = chatbot.chatty_boi(result, query)
        response = chatbot.open_chatty_boi(result, query)
        answer = ""
        for chunk in response:
            if not chunk['done']: # Use along side ollama
            # if chunk.choices[0].delta.content:
                sys.stdout.write(chunk['message']['content'])
                # sys.stdout.write(chunk.choices[0].delta.content)
                sys.stdout.flush()
        print()


# python main.py docs/NIPS-2017-attention-is-all-you-need-Paper.pdf