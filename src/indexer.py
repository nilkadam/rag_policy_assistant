import faiss

class FaissIndexer:
    def __init__(self, dim):
        self.index = faiss.IndexFlatIP(dim)

    def add(self, embeddings):
        self.index.add(embeddings)

    def search(self, query_embedding, top_k=3):
        scores, indices = self.index.search(query_embedding, top_k)
        return scores, indices