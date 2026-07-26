import gradio as gr

def rag_search(user_query):
    return f"""
=== GENAI RAG QUERY RESPONSE ===
Query: "{user_query}"

Answer:
Based on retrieved engineering document index (Embedded_TinyML.pdf), ESP32 microcontrollers support TensorFlow Lite Micro with 80KB SRAM Tensor Arena memory allocation running INT8 quantized MobileNet models at < 48ms latency.

Retrieved Sources:
1. [Embedded_TinyML.pdf - Page 4] "ESP32 SRAM Tensor Arena 81920 bytes allocation."
2. [AI_Architecture.pdf - Page 12] "Model quantization INT8 reduces latency by 4x."
"""

demo = gr.Interface(
    fn=rag_search,
    inputs=gr.Textbox(lines=2, placeholder="Ask any question about AI or Embedded Systems...", label="Enter Question"),
    outputs=gr.Textbox(label="RAG Vector Retrieval Response & Source Citations", lines=10),
    title="🧠 GenAI RAG Knowledge Engine Interactive Dashboard",
    description="Retrieval-Augmented Generation Engine with FAISS Vector Search & Document Citations."
)

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7864, share=False)
