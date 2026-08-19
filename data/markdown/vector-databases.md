\# Vector Databases



A vector database is a specialized database designed to store and search high-dimensional vectors (embeddings) efficiently, rather than traditional structured data like rows and columns. Examples include FAISS, ChromaDB, Pinecone, and Weaviate.



The core problem vector databases solve is nearest neighbor search: given a query vector, find the most similar vectors in a large collection. Doing this with a brute-force comparison against every stored vector becomes extremely slow as the collection grows to millions of items, so vector databases use approximate nearest neighbor (ANN) algorithms to make this fast.



FAISS, developed by Meta, uses techniques like inverted file indexes and quantization to speed up search while trading off a small amount of accuracy for large gains in speed. ChromaDB is a simpler, developer-friendly vector store often used for smaller-scale local projects, with built-in support for storing metadata alongside vectors.



In a RAG system, the vector database stores embeddings of document chunks along with metadata (like source filename or page number). When a query comes in, its embedding is compared against all stored embeddings to retrieve the most relevant chunks, which are then passed to the LLM as context.

