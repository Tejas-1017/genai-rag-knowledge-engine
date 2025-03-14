import chromadb
from pathlib import Path

class VectorStoreManager:
    def __init__(self, db_path="./chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name="enterprise_knowledge")
        print(f"[CHROMA] Connected to persistent vector store at '{db_path}'")

    def add_documents(self, ids, embeddings, documents, metadatas=None):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )

    def query(self, query_embedding, n_results=4):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
