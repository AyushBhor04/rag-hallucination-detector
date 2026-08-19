\# LoRA: Low-Rank Adaptation



LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that makes it much cheaper to fine-tune large language models. Full fine-tuning requires updating all of a model's weights, which for models with billions of parameters demands huge amounts of GPU memory and compute.



LoRA works by freezing the original pretrained weights entirely and instead injecting small, trainable low-rank matrices into specific layers of the model (commonly the attention layers). During training, only these small added matrices are updated, while the original weights stay unchanged. Because these matrices are much smaller than the full weight matrices, the number of trainable parameters drops dramatically, often by more than 90 percent.



This has several practical benefits: training requires far less GPU memory, checkpoints are much smaller since only the LoRA weights need to be saved, and multiple LoRA adapters can be trained for different tasks and swapped in and out on top of the same base model.



LoRA has become one of the most popular fine-tuning methods for open-source LLMs because it makes customizing large models feasible on consumer-grade hardware, rather than requiring expensive multi-GPU clusters.

