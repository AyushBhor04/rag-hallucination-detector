\# Retrieval-Augmented Generation (RAG)



RAG is a technique that combines information retrieval with text generation to make LLM outputs more accurate and grounded in real data. A plain LLM only knows what it learned during training, so it can produce outdated, incomplete, or hallucinated answers, especially for niche or recent topics.



The RAG pipeline works in four steps: first, the user's query is converted into a vector embedding. Second, that embedding is used to search a vector database for the most semantically similar chunks of text from a document collection. Third, these retrieved chunks are inserted into the LLM's prompt as context. Fourth, the LLM generates an answer using both the original query and the retrieved context, rather than relying purely on its internal knowledge.



This matters because it lets the LLM answer questions about documents it was never trained on, and it reduces hallucination since the model is encouraged to base its answer on the retrieved text. RAG systems can also cite sources, since the retrieved chunks are traceable back to specific documents.



A well-built RAG system also needs a way to check whether the generated answer is actually supported by the retrieved context, since the LLM can still ignore the context and hallucinate anyway.

