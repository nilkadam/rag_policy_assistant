<<<<<<< HEAD
# Enterprise RAG

This project implements a Retrieval-Augmented Generation (RAG) pipeline for enterprise policy documents. It loads, chunks, embeds, indexes, and retrieves document content to answer user queries using a generative model.

## Project Structure

```
enterprise_rag/
│   main.py
│   README.md
│   requirements.txt
│
├───data/
│       policies.txt
│
└───src/
        chunking.py
        embedder.py
        evaluator.py
        generator.py
        indexer.py
        ingestion.py
        rag_pipeline.py
        retriever.py
```

## Prerequisites

- Python 3.8 or higher
- [Git](https://git-scm.com/download/win) (for version control)
- pip (Python package manager)

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/enterprise-rag.git
   cd enterprise-rag
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Prepare your data**
   - Place your policy documents in the `data/policies.txt` file. You can replace or update this file as needed.

5. **Run the application**
   ```sh
   python main.py
   ```
   - The program will prompt you to ask questions about the policy documents. Type your question and press Enter.
   - Type `exit` to quit the application.

## How It Works

- **Ingestion:** Loads policy documents from the data folder.
- **Chunking:** Splits the text into manageable chunks.
- **Embedding:** Converts text chunks into vector embeddings.
- **Indexing:** Stores embeddings in a FAISS index for efficient retrieval.
- **Retrieval:** Finds relevant chunks based on user queries.
- **Generation:** Uses a generative model to answer questions using retrieved content.

## Customization
- To use your own documents, replace the contents of `data/policies.txt`.
- You can modify or extend the modules in the `src/` directory for custom chunking, embedding, or retrieval logic.

## License

This project is for educational and research purposes. Please check the repository license for more details.
=======
# rag_policy_assistant
This project implements a Retrieval-Augmented Generation (RAG) pipeline for enterprise policy documents. It loads, chunks, embeds, indexes, and retrieves document content to answer user queries using a generative model.
>>>>>>> 19af45efa63862d8c6ec9ed5813c436b16539505
