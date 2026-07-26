import numpy as np

class FAISSVectorStore:
    def __init__(self, dim=384):
        self.dim = dim
        print(f"[FAISS] Initialized vector index with dimension {dim}.")
    def search(self, query_vec, k=3):
        return [{"id": 1, "score": 0.94, "text": "TinyML deployment on ESP32 SRAM arena."}]
