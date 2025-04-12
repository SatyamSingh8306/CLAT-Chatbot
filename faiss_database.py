from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader,PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
load_dotenv()

DB_FAISS_PATH = "vectorstores/db_faiss"
HF_API_KEY = os.environ.get("HF_API_KEY")
PDF_PATH = "./pdfs/"

def loadDocuments(path):

    loader = DirectoryLoader(
        path=PDF_PATH,
        glob="*.pdf",
        loader_cls=PyMuPDFLoader
    )

    documents = loader.load()
    return documents
def textSplitter(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks


def embeddingModel(model_name="sentence-transformers/all-MiniLM-L6-v2", HF_API_KEY=os.environ.get("HF_API_KEY")):
    embedding_model = HuggingFaceEmbeddings(
    model_name = model_name,
    model_kwargs = {"device": "cpu"},
    encode_kwargs = {'api_key': HF_API_KEY}
    )
    return embedding_model

def createDatabase(chunks, embedding_model):
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    documents = loadDocuments(PDF_PATH)
    chunks = textSplitter(documents)
    embedding_model = embeddingModel()
    createDatabase(chunks, embedding_model)



