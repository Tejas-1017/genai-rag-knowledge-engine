class RAGKnowledgeEngine:
    def __init__(self):
        self.knowledge_base = [
            "TinyML quantizes FP32 weights to INT8 to fit microcontroller SRAM.",
            "FreeRTOS Core 0 is optimized for sensor sampling and Core 1 for BLE telemetry.",
            "Isolation Forest detects multivariate mechanical anomalies without labeled fault data."
        ]
    def query(self, prompt):
        context = "\n".join(self.knowledge_base)
        response = f"Answer generated from local RAG context:\nBased on your query '{prompt}', the knowledge engine retrieved:\n- {self.knowledge_base[0]}"
        return response, [self.knowledge_base[0]]
