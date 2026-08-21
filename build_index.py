"""
build_index.py
Loads chunks.json, generates embeddings for each chunk using
sentence-transformers, and stores them in a persistent local
ChromaDB collection for semantic search.
"""

import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

# ---------- CONFIG ----------
CHUNKS_FILE = Path("data/processed/chunks.json")
CHROMA_DB_DIR = "chroma_db"          # folder where Chroma saves its data
COLLECTION_NAME = "rag_documents"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
BATCH_SIZE = 32                       # how many chunks we embed at once


def load_chunks():
    """Loads the chunk list produced by ingest.py"""
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    print(f"Loaded {len(chunks)} chunks from {CHUNKS_FILE}")
    return chunks


def build_index(chunks):
    # ---------- Load embedding model ----------
    print(f"Loading embedding model: {EMBEDDING_MODEL_NAME} ...")
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    # ---------- Set up persistent ChromaDB client ----------
    # PersistentClient saves data to disk in CHROMA_DB_DIR, so the
    # index survives between script runs — we only need to build it once.
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

    # If a collection with this name already exists (e.g. from a previous
    # run), delete it first so we don't get duplicate entries.
    existing_collections = [c.name for c in client.list_collections()]
    if COLLECTION_NAME in existing_collections:
        print(f"Collection '{COLLECTION_NAME}' already exists — deleting to rebuild fresh.")
        client.delete_collection(COLLECTION_NAME)

    collection = client.create_collection(name=COLLECTION_NAME)

    # ---------- Embed and add chunks in batches ----------
    total = len(chunks)
    for start in range(0, total, BATCH_SIZE):
        batch = chunks[start:start + BATCH_SIZE]

        texts = [c["text"] for c in batch]
        ids = [c["chunk_id"] for c in batch]
        metadatas = [
            {
                "source_file": c["source_file"],
                "format": c["format"],
                "chunk_index": c["chunk_index"]
            }
            for c in batch
        ]

        # Generate embeddings for this batch
        embeddings = model.encode(texts, show_progress_bar=False).tolist()

        # Add to ChromaDB: vectors + original text + metadata, keyed by id
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )

        done = min(start + BATCH_SIZE, total)
        print(f"  Embedded and stored {done}/{total} chunks")

    print(f"\nDONE. Collection '{COLLECTION_NAME}' now has {collection.count()} items.")
    print(f"Stored at: {CHROMA_DB_DIR}/")


def main():
    chunks = load_chunks()
    build_index(chunks)


if __name__ == "__main__":
    main()