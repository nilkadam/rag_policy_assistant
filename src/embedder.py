from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def encode(self, texts):
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return np.array(embeddings).astype("float32")