\# Prompt Engineering: Chain-of-Thought and Few-Shot



Prompt engineering is the practice of designing input prompts to get better, more reliable outputs from an LLM without changing its underlying weights.



Chain-of-thought (CoT) prompting encourages the model to reason step by step before giving a final answer, rather than jumping straight to a conclusion. This is often done by explicitly asking the model to "think step by step" or by providing example reasoning chains in the prompt. CoT has been shown to significantly improve performance on tasks requiring logic, arithmetic, or multi-step reasoning, because it gives the model room to work through intermediate steps rather than trying to predict the final answer in one shot.



Few-shot prompting provides the model with a small number of example input-output pairs directly in the prompt before asking it to handle a new case. This helps the model understand the expected format, style, or reasoning pattern without any fine-tuning. Zero-shot prompting, by contrast, gives no examples at all and relies purely on instructions.



In a RAG system, prompt engineering is also used to instruct the model to only answer based on the provided context, and to explicitly say when the context doesn't contain enough information, which supports the groundedness and refusal behavior of the system.

