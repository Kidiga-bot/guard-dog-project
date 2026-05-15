---
type: concept
tags:
  - security
  - llm
  - ai
created: 2026-05-15
provenance: 1.0
---

# Prompt Injection Detection

Prompt injection is a security vulnerability where an attacker provides crafted input to an LLM to override its system instructions or extract sensitive data.

## Detection Strategy: Binary Classification
Rather than using complex heuristics, a small language model (like DistilBERT) can be fine-tuned as a binary classifier.

- **Input**: The raw user prompt.
- **Output**: A probability distribution over two classes:
    - **Class 0 (Safe)**: Benign user requests.
    - **Class 1 (Malicious)**: Attempts to bypass instructions (e.g., "Ignore previous instructions").

## Advantages
- **Low Latency**: Small models (<500MB) can run as a fast pre-filter before the main LLM.
- **Confidence Scoring**: Using Softmax allows for setting a threshold (e.g., only block if confidence > 95%).

## Implementation
- [[Guard Dog]]


Up: [[Index - Engineering Concepts]]
