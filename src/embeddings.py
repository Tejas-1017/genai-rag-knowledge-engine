from sentence_transformers import SentenceTransformer

class EmbeddingManager:
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        print(f"[EMBEDDINGS] Loading model {model_name}...")
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text):
        return self.model.encode(text).tolist()

    def embed_documents(self, docs):
        return self.model.encode(docs).tolist()
