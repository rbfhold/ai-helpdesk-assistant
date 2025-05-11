import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
load_dotenv()


CHROMA_DB_PATH = "./chroma_db"

def load_qa_chain():
    # Load vector store
    vectordb = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=OpenAIEmbeddings()
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    # Use GPT-4 or GPT-3.5
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

def ask_question(query: str):
    qa = load_qa_chain()
    result = qa(query)
    answer = result["result"]

    # Extract source snippets
    sources = []
    for doc in result["source_documents"]:
        metadata = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page", "Unknown page")
        snippet = doc.page_content.strip()
        sources.append(f"📄 **{metadata}**, page {page}:\n> {snippet}")

    return answer, sources