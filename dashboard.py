import gradio as gr
from src.rag_pipeline import RAGKnowledgeEngine
rag = RAGKnowledgeEngine()
def ask_rag(question):
    answer, sources = rag.query(question)
    return answer, "\n".join([f"• {s}" for s in sources])
demo = gr.Interface(
    fn=ask_rag,
    inputs=gr.Textbox(label="Ask AI Knowledge Engine", value="How does TinyML quantization work on ESP32?"),
    outputs=[gr.Textbox(label="Synthesized RAG Response", lines=4), gr.Textbox(label="Retrieved Source Chunks", lines=2)],
    title="🧠 GenAI RAG Knowledge Engine (Llama-3 + ChromaDB)"
)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7876, share=False)
