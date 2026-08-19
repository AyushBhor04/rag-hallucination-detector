\# Evaluating RAG Systems



Evaluating a RAG system requires looking at both the retrieval component and the generation component separately, since a failure in either can produce a bad final answer.



For retrieval, common metrics include precision (what fraction of retrieved chunks are actually relevant to the query) and recall (what fraction of all relevant chunks in the corpus were successfully retrieved). Higher precision means less irrelevant noise passed to the LLM, while higher recall means fewer relevant chunks are missed entirely.



For generation, groundedness (also called faithfulness) measures whether the generated answer is actually supported by the retrieved context, rather than being invented by the model. This can be checked using methods like natural language inference (NLI) models, which classify whether the context entails, contradicts, or is neutral toward the generated answer, or by measuring semantic overlap between the answer and the context.



Answer relevance measures whether the generated answer actually addresses the user's question, since an answer can be perfectly grounded in the context but still fail to answer what was asked.



A robust RAG system evaluation combines all three: retrieval quality, groundedness, and answer relevance, rather than just checking whether the final answer "looks right" to a human reader.

