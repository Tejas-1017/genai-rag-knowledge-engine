# GenAI RAG Document Intelligence Engine 🧠⚡

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-00F3FF)](https://langchain.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-9D00FF)](https://trychroma.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi)](https://fastapi.tiangolo.com)

An enterprise-grade Retrieval-Augmented Generation (RAG) system utilizing quantized local LLMs (Llama 3 / Mistral via Ollama) and ChromaDB vector embeddings for real-time semantic document search and intelligent QA.

---

## 🌟 Key Features

- 🔍 **Vector Embeddings & Semantic Search**: Uses `bge-small-en-v1.5` embeddings for high-precision vector retrieval.
- ⚡ **Local Quantized LLM Inference**: Fully private local LLM generation via INT4 quantization (< 1.2s time-to-first-token).
- 🚀 **FastAPI Backend & Streaming UI**: Provides asynchronous endpoints for document ingestion and streaming chat completions.

---

## 💻 Quick Start

### 1. Installation
```bash
git clone https://github.com/Tejas-1017/genai-rag-knowledge-engine.git
cd genai-rag-knowledge-engine
pip install -r requirements.txt
```

### 2. Run Query Engine
```bash
python src/rag_pipeline.py --query "What are the latency specs for Edge AI models?"
```

---

## 👤 Author
**Tejas Rohit Kharkar**  
AI & Machine Learning Engineer | [LinkedIn](https://linkedin.com/in/tejas-kharkar-tech) | [GitHub](https://github.com/Tejas-1017)
