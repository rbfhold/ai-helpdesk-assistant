
# app/app.py

import streamlit as st
import os
import subprocess
from rag_chain import ask_question
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

st.set_page_config(page_title="AI Helpdesk Assistant", page_icon="🧠")
st.title("🧠 AI-Powered Helpdesk Assistant")
st.markdown("🛠 DEBUG: upload block should be visible below this line")
st.markdown("Ask any question related to internal FAQs, policies, or support procedures.")

# --- File Upload Section ---
st.subheader("📎 Upload a New PDF to Update Knowledge Base")
uploaded_file = st.file_uploader("Upload a PDF file:", type=["pdf"])

if uploaded_file is not None:
    save_path = os.path.join("data", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully.")

    with st.spinner("📦 Rebuilding vector store..."):
        try:
            subprocess.run(["python", "utils/ingest.py"], check=True)
            st.success("✅ Vector store updated.")
        except subprocess.CalledProcessError:
            st.error("❌ Error during ingestion. Please check the logs.")

# --- Chat History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- User Input ---
user_query = st.text_input("🔍 Your question:", placeholder="e.g., How do I access my VPN?", key="input")

# --- Handle Submission ---
if user_query:
    with st.spinner("Thinking..."):
        answer, sources = ask_question(user_query)
        st.session_state.chat_history.append((user_query, answer, sources))

# --- Display Chat History ---
if st.session_state.chat_history:
    st.markdown("---")
    for q, a, sources in reversed(st.session_state.chat_history):
        st.markdown(f"**🧑 You:** {q}")
        st.markdown(f"**🤖 Assistant:** {a}")
        with st.expander("📚 View Sources"):
            for src in sources:
                st.markdown(src, unsafe_allow_html=True)
        st.markdown("---")
