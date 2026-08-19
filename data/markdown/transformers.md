\# Transformers and Self-Attention



Transformers are a neural network architecture introduced in the 2017 paper "Attention Is All You Need." Before transformers, models like RNNs and LSTMs processed text sequentially, one token at a time, which made them slow to train and bad at capturing long-range dependencies in text.



Self-attention solves this by letting every token in a sequence look at every other token directly, regardless of distance, and learn how much to "attend" to each one. For each token, the model computes a Query, Key, and Value vector. The attention score between two tokens is based on the similarity between one token's Query and another's Key, and this score determines how much of the Value gets passed forward.



Because attention can be computed in parallel across the whole sequence, transformers train much faster than RNNs on modern hardware (GPUs/TPUs). Multi-head attention runs several attention computations in parallel, letting the model capture different types of relationships (syntax, meaning, position) at once.



Transformers became the foundation for nearly all modern large language models, including BERT, GPT, and LLaMA, because they scale well with more data and compute.

