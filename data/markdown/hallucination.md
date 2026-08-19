\# Why LLMs Hallucinate



Hallucination refers to an LLM generating text that sounds plausible and confident but is factually incorrect or unsupported by any real source. This happens because LLMs are fundamentally next-token predictors: they generate text by predicting the most statistically likely next word given the previous context, not by checking facts against a verified knowledge base.



Several factors contribute to hallucination. The model may not have seen relevant information during training, the training data itself may contain errors, or the model may blend information from multiple unrelated contexts in a way that sounds coherent but is wrong. LLMs also have no built-in mechanism to say "I don't know" by default, they are trained to always produce a plausible-sounding continuation.



RAG helps reduce hallucination by grounding the model's answer in retrieved, real documents rather than relying purely on internal memorized knowledge. However, RAG alone doesn't eliminate hallucination entirely, the LLM can still ignore the retrieved context and generate an answer that isn't actually supported by it.



This is why a groundedness or confidence scoring step is valuable: after generating an answer, a separate check compares the answer against the retrieved context to verify the answer is actually supported by it, and flags or refuses the answer if it isn't.

