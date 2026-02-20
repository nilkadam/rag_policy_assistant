class RAGPipeline:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def build_prompt(self, query, contexts):
        context_text = "\n\n".join(contexts)

        return f"""
You are a financial compliance assistant.
Use ONLY the context below.

Context:
{context_text}

Question:
{query}

Answer:
"""

    def run(self, query):
        contexts = self.retriever.retrieve(query)
        prompt = self.build_prompt(query, contexts)
        return self.generator.generate(prompt)