import os
os.environ['OPENAI_API_KEY'] = "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"

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("docs/Agent_Sai_Srinivasa_Athreya_Script.pdf")
texts = loader.load_and_split()

# loader = TextLoader('./docs/sample_doc.txt')
# documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever()

tool = create_retriever_tool(
    retriever, 
    "Agent_Sai_Srinivas_Athreya",
    "Searches and returns documents regarding Agent Sai Srinivas Athreya."
)
tools = [tool]

llm = ChatOpenAI(temperature = 0)
agent_executor = create_conversational_retrieval_agent(llm, tools, verbose=True)
while True:
    input_text = input("Hey, Sup?")
    result = agent_executor({"input": input_text})
    print(result["output"])