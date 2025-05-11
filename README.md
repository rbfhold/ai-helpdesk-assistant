# 🧠 AI Helpdesk Assistant

An AI-powered helpdesk chatbot that answers internal FAQ, policy, and support questions from PDF documents using OpenAI + LangChain + ChromaDB + Streamlit.

## 🚀 Live Demo

🔗 [Add your Streamlit Cloud link here after deployment]

---

## 📦 Features

- 📎 Upload your own PDFs (FAQs, manuals, policies)
- 🔍 Retrieval-Augmented Generation (RAG) with LangChain + ChromaDB
- 🤖 Answers powered by OpenAI GPT-4
- 💬 Live chat history with expandable source citations
- 🖥️ Streamlit-based frontend – fast to deploy and easy to use

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- OpenAI API

---

## 📁 Project Structure

```
├── app/
│   ├── app.py           # Streamlit UI
│   └── rag_chain.py     # RAG logic and OpenAI call
├── utils/
│   └── ingest.py        # PDF loader + vector store builder
├── data/                # Folder for uploaded PDF files
├── requirements.txt     # Python dependencies
└── .env (excluded)
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/ai-helpdesk-assistant.git
cd ai-helpdesk-assistant
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API key to `.env`**
```dotenv
OPENAI_API_KEY=your-key-here
```

5. **Run the app**
```bash
streamlit run app/app.py
```

---

## 🔐 Deployment Notes

On **Streamlit Cloud**:
- Set `app/app.py` as your app entry point
- Use the **Secrets Manager** to store `OPENAI_API_KEY`

---

## 📄 License

MIT License

---

Created with ❤️ by [Your Name]