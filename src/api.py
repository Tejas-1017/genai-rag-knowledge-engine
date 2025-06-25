from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.rag_pipeline import RAGPipeline

app = FastAPI(title="GenAI RAG Knowledge Engine API", version="1.0.0")
rag = RAGPipeline()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"engine": "GenAI RAG", "status": "active", "db": "ChromaDB", "model": "Llama 3 8B"}

@app.post("/query")
def query_rag(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    return rag.answer_question(request.query)
