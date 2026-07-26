from fastapi import FastAPI
app = FastAPI(title="GenAI RAG Knowledge Engine API")

@app.get("/")
def info():
    return {"engine": "GenAI RAG Pipeline", "status": "ACTIVE"}
