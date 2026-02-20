from src.ingestion import load_documents
from src.chunking import chunk_text
from src.embedder import Embedder
from src.indexer import FaissIndexer
from src.retriever import Retriever
from src.generator import Generator
from src.rag_pipeline import RAGPipeline

# Load data
text = load_documents("data/policies.txt")

# Chunk
chunks = chunk_text(text)

# Embed
embedder = Embedder()
embeddings = embedder.encode(chunks)

# Index
indexer = FaissIndexer(embeddings.shape[1])
indexer.add(embeddings)

# Retrieve + Generate
retriever = Retriever(embedder, indexer, chunks)
generator = Generator()
rag = RAGPipeline(retriever, generator)

while True:
    query = input("\nAsk a question (or type exit): ")
    if query.lower() == "exit":
        break

    answer = rag.run(query)
    print("\nAnswer:\n", answer)