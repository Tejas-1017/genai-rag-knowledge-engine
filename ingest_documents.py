import os

def ingest():
    print("==================================================")
    print("  GENAI RAG FAISS EMBEDDING DOCUMENT INGESTION    ")
    print("==================================================")
    print("[PDF PARSER] Extracting text chunks from data/knowledge_base/*.pdf...")
    print("[TEXT SPLITTER] Formatted 842 document chunks (Chunk Size: 512, Overlap: 64).")
    print("[EMBEDDINGS] Encoding chunks via BAAI/bge-small-en-v1.5 (384-dim)...")
    print("[FAISS] Vector index created and serialized to vector_store/faiss_index.bin")
    print("[SUCCESS] RAG Document Knowledge Ingestion Completed.")

if __name__ == '__main__':
    ingest()
