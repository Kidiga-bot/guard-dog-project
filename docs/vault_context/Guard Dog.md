---
type: project
status: completed
tags:
  - ai
  - security
  - prompt-injection
  - distilbert
created: 2026-05-15
project: Guard Dog
provenance: 1.0
---

# Guard Dog Project

A lightweight prompt injection detector trained on `distilbert-base-uncased`. This project demonstrates a full local machine learning pipeline on Apple Silicon (M5).

## Overview
The project consists of five sequential stages:
1. **Data Loading**: Fetching the `deepset/prompt-injections` dataset from Hugging Face.
2. **Tokenization**: Converting English text into numerical IDs using the DistilBERT tokenizer.
3. **Data Preparation**: Applying padding and truncation to create uniform input grids.
4. **Fine-Tuning**: Retraining the classification head of DistilBERT for binary security labels (Safe vs. Malicious).
5. **Inference**: Running real-world test prompts through the custom AI brain to detect attacks.

## Hardware Configuration
- **Machine**: MacBook Air M5
- **Memory**: 16GB Unified Memory
- **Acceleration**: Apple Neural Engine & Metal Performance Shaders (MPS)

## Technical Architecture
- **Base Model**: `distilbert-base-uncased`
- **Labels**: 2 (0: Safe, 1: Malicious)
- **Training Logic**: [[MPS Accelerated Fine-Tuning]]
- **Security Concept**: [[Prompt Injection Detection]]

## Sources
- Path: `/Users/raykidiga/Desktop/guard_dog_ptoject`
- Author: [[Personal]]
- Initial Narrative: [[My first trained ai model]]


Up: [[Index - Engineering Projects]]
