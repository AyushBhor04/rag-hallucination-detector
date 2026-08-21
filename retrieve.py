"""
retrieve.py
Takes a user query, embeds it using the same model used for the
document chunks, and retrieves the top-k most similar chunks from
ChromaDB along with their source metadata.
"""

from sentence_transformers import SentenceTransformer
import chromadb

CHROMA_DB_DIR = "chroma_db"
COLLECTION_NAME = "rag_documents"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 5  # how many chunks to retrieve per query


def load_retriever():
    """
    Loads the embedding model and connects to the existing
    persistent ChromaDB collection (built in Step 4).
    """
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    collection = client.get_collection(name=COLLECTION_NAME)
    return model, collection


def retrieve(query: str, model, collection, top_k=TOP_K):
    """
    Embeds the query and returns the top_k most similar chunks,
    each with its text, source metadata, and similarity distance.
    """
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    # Chroma returns results as parallel lists inside a dict.
    # We reshape this into a simpler list of dicts for easier use later.
    retrieved_chunks = []
    for i in range(len(results["ids"][0])):
        retrieved_chunks.append({
            "chunk_id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "source_file": results["metadatas"][0][i]["source_file"],
            "format": results["metadatas"][0][i]["format"],
            "distance": results["distances"][0][i]  # lower = more similar
        })

    return retrieved_chunks


def main():
    model, collection = load_retriever()

    print("Retrieval test mode. Type a question (or 'quit' to exit).\n")
    while True:
        query = input("Question: ").strip()
        if query.lower() in ("quit", "exit"):
            break
        if not query:
            continue

        results = retrieve(query, model, collection)

        print(f"\nTop {len(results)} results:\n")
        for rank, r in enumerate(results, start=1):
            print(f"[{rank}] source: {r['source_file']} ({r['format']}) | distance: {r['distance']:.4f}")
            print(f"    {r['text'][:200]}...")  # preview first 200 chars
            print()


if __name__ == "__main__":
    main()