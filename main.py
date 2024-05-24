import os
from utils import ChatBot, TextUtils, VectorDBUtils
os.environ["OPENAI_API_KEY"] = "sk-proj-TgfdYEYMUR2LGiu5frtcT3BlbkFJMDbYpPjLsPlpRkfM0dz5"

if __name__=="__main__":

    text_object = TextUtils()
    vector_object = VectorDBUtils()
    extracted_text = text_object.extract_text("docs/NIPS-2017-attention-is-all-you-need-Paper.pdf")
    chunked_text = text_object.chunk_pdf(extracted_text)
    vector_fetch = vector_object.create_embeddings(chunked_text)
    result = vector_fetch.similarity_search("Why do I even need attention?", k=1)
    chatbot = ChatBot()
    print(chatbot.chatty_boi(result, query="Why do I even need attention?"))
    print(len(result))
    