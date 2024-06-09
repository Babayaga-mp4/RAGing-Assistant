from typing import List
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents.base import Document
# from langchain_community.document_loaders import PyMuPDFLoader

from langchain_community.document_loaders import PyPDFLoader


from constants import MESSAGE_TEMPLATE

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
    
    def build_history(conversation_key, query, answer, context):
        formatted_message = {
            "role": MESSAGE_TEMPLATE["role"],
            "content": MESSAGE_TEMPLATE["content"].format(query=query, context=context)
        }
        formatted_answer = {"role": "user", "content": f"{answer}"}
        return formatted_message, formatted_answer