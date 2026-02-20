class Retriever:
    def __init__(self, embedder, indexer, chunks):
        self.embedder = embedder
        self.indexer = indexer
        self.chunks = chunks

    def retrieve(self, query):
        query_embedding = self.embedder.encode([query])
        scores, indices = self.indexer.search(query_embedding, top_k=3)

        results = []
        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results