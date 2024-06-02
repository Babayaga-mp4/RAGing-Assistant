# Chunk down pdf
from typing import List
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents.base import Document
# from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import Qdrant
from langchain_community.document_loaders import PyPDFLoader
# from openai import embeddings
from openai import OpenAI, Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_message import ChatCompletionMessage

import ollama

class TextUtils():
    def __init__(self) -> None:
        pass

    def chunk_pdf(self, docs) -> List[Document]:
        text_splitter = CharacterTextSplitter(
            separator = "\n\n",
            chunk_size = 256,
            chunk_overlap  = 20
        )
        docs = text_splitter.split_documents(docs)
        return docs
    
    def extract_text(self, path) -> List[Document]:
        # The output from the loader is alread chunked in itself
        # loader = PyMuPDFLoader(path)
        # data = loader.load()
        loader = PyPDFLoader(path)
        data = loader.load_and_split()
        return data

class VectorDBUtils():
    def __init__(self) -> None:
        self.qdrant = None
        pass
    
    def _get_embeddings(self) -> OpenAIEmbeddings:
        return OpenAIEmbeddings()
    
    def create_embeddings(self, docs) -> Qdrant:
        """ query = "What did the president say about Ketanji Brown Jackson"
            found_docs = qdrant.similarity_search(query) """
        return Qdrant.from_documents(
                        documents=docs,
                        embedding=self._get_embeddings(),
                        location=":memory:",  # Local mode with in-memory storage only
                        collection_name="my_documents",
                        )

class ChatBot():
    def __init__(self) -> None:
        self.client = OpenAI()
        pass

    def chatty_boi(self, context, query) -> Stream[ChatCompletionChunk]:
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are witty and cheesey assistant, skilled in explaining complex concepts with creative flair.\
              You will be assisted by AI which bring you the context behind the user's queries"},
            {"role": "user", "content": f"{query}, ------------------------------ Here's some context to help you out {context}"}
        ],
        stream=True
        )

        return completion
    
    def open_chatty_boi(self, context, query):
        # Handles Open Source LLMs
        completion = ollama.chat(
            model='phi3:3.8b-mini-128k-instruct-q2_K',
            messages=[
                    {"role": "system", "content": "You are witty and cheesey assistant, skilled in explaining complex concepts with creative flair.\
                    You will be assisted by AI which bring you the context behind the user's queries"},
                    {"role": "user", "content": f"{query}, ------------------------------ Here's some context to help you out {context}"}
                ],
            stream=True,
        )

        return completion