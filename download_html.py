import requests

urls = {
    "post1": "https://huggingface.co/blog/embedding-quantization",
    "post2": "https://huggingface.co/blog/peft-beyond-lora",
    "post3": "https://jalammar.github.io/illustrated-transformer/",
    "post4": "https://jalammar.github.io/illustrated-bert/",
    "post5": "https://jalammar.github.io/illustrated-gpt2/",
    "post6": "https://www.pinecone.io/learn/retrieval-augmented-generation/",
    "post7": "https://www.pinecone.io/learn/series/rag/rerankers/",
    "post8": "https://weaviate.io/blog/chunking-strategies-for-rag",
    "post9": "https://weaviate.io/blog/advanced-rag",
    "post10": "https://deepmind.google/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/"
}

for name, url in urls.items():
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        r.raise_for_status()

        with open(f"data/html/{name}.html", "w", encoding="utf-8") as f:
            f.write(r.text)

        print(f"Saved {name}")

    except Exception as e:
        print(f"Failed {name}: {e}")