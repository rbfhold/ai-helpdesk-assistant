# utils/ingest.py

import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv


load_dotenv()  # Load OpenAI key from .env
os.getenv("OPENAI_API_KEY")

DATA_PATH = "./data"
CHROMA_DB_PATH = "./chroma_db"

def load_documents():
    docs = []
    for filename in os.listdir(DATA_PATH):
        filepath = os.path.join(DATA_PATH, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
        elif filename.endswith(".md") or filename.endswith(".txt"):
            loader = TextLoader(filepath)
        else:
            continue
        docs.extend(loader.load())
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)

def create_chroma_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_DB_PATH)
    vectordb.persist()
    print(f"✅ Vector store saved to {CHROMA_DB_PATH}")

if __name__ == "__main__":
    print("📄 Loading documents...")
    raw_docs = load_documents()
    print(f"✅ Loaded {len(raw_docs)} documents")

    print("✂️ Splitting documents into chunks...")
    chunks = split_documents(raw_docs)
    print(f"✅ Created {len(chunks)} chunks")

    print("📦 Creating vector store with OpenAI embeddings...")
    create_chroma_vectorstore(chunks)
