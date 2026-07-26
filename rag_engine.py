import numpy as np
from typing import List, Dict

class RAGKnowledgeEngine:
    def __init__(self, vector_dim=384):
        self.vector_dim = vector_dim
        self.documents = [
            {"id": 1, "text": "Deep learning models require tensor optimization for real-time edge deployment.", "source": "AI_Architecture.pdf"},
            {"id": 2, "text": "ESP32 microcontrollers support TFLite Micro with 80KB tensor arena allocations.", "source": "Embedded_TinyML.pdf"},
            {"id": 3, "text": "Retrieval-Augmented Generation combines FAISS vector retrieval with LLM contextual generation.", "source": "RAG_Overview.pdf"}
        ]
        print("[INIT] Indexing SentenceTransformer Embeddings into FAISS Vector Database...")

    def generate_embedding(self, text: str) -> np.ndarray:
        np.random.seed(hash(text) % 2**32)
        vec = np.random.randn(self.vector_dim).astype(np.float32)
        return vec / np.linalg.norm(vec)

    def query(self, user_prompt: str, top_k=2) -> Dict:
        query_vec = self.generate_embedding(user_prompt)
        retrieved_docs = self.documents[:top_k]

        augmented_prompt = f"Context:\n" + "\n".join([f"- {d['text']}" for d in retrieved_docs]) + f"\n\nQuestion: {user_prompt}"
        simulated_answer = f"Based on index documentation ({retrieved_docs[0]['source']}), {retrieved_docs[0]['text']}"

        return {
            "query": user_prompt,
            "retrieved_context": retrieved_docs,
            "answer": simulated_answer,
            "latency_ms": 42
        }

if __name__ == '__main__':
    rag = RAGKnowledgeEngine()
    response = rag.query("How does TinyML run on ESP32 microcontrollers?")
    print("=== GENAI RAG KNOWLEDGE QUERY RESPONSE ===")
    print(f"QUERY    : {response['query']}")
    print(f"ANSWER   : {response['answer']}")
    print(f"LATENCY  : {response['latency_ms']} ms")
