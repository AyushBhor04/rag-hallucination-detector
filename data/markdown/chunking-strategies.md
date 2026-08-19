\# Chunking Strategies for RAG



Before documents can be embedded and stored in a vector database, they need to be split into smaller pieces called chunks. This is necessary because embedding models have a maximum input length, and because retrieving huge documents in full would give the LLM too much irrelevant text alongside the relevant part.



Choosing the right chunk size involves a tradeoff. If chunks are too small, they may lose important context, a sentence taken in isolation might not make sense without the paragraph around it. If chunks are too large, they can contain a mix of relevant and irrelevant information, which dilutes the embedding's specificity and can hurt retrieval accuracy.



A common approach is fixed-size chunking with overlap, splitting text into chunks of a set number of tokens or characters (for example 300-500 tokens), with a small overlap (like 50 tokens) between consecutive chunks so that context isn't lost at chunk boundaries.



More advanced approaches use semantic chunking, splitting text at natural boundaries like paragraphs, sections, or headers, so each chunk represents a coherent idea. For a format-agnostic RAG pipeline handling PDF, HTML, and Markdown, chunking strategy also needs to account for structural noise specific to each format before splitting.

