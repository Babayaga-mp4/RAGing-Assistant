from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import Qdrant

class VectorDBUtils():
    def __init__(self) -> None:
        self.qdrant = None
        pass
    
    def _get_embeddings(self) -> OpenAIEmbeddings:
        return OpenAIEmbeddings()
    
    def create_embeddings(self, docs) -> Qdrant:
        # The memory will be cleared everytime the application is down.
        return Qdrant.from_documents(
                        documents=docs,
                        embedding=self._get_embeddings(),
                        location=":memory:",  # Local mode with in-memory storage only
                        collection_name="my_documents",
                        )
