---
type: trap
project: Guard Dog
tags:
  - dependency
  - error
  - huggingface
created: 2026-05-15
provenance: 1.0
---

# ML Environment Dependencies

Common pitfalls encountered when setting up a local machine learning environment on macOS.

## Missing 'accelerate' Library
**Problem**: The Hugging Face `Trainer` crashes on Mac when trying to initialize hardware devices.
**Error**: `ImportError: Using the Trainer with PyTorch requires accelerate>=1.1.0`
**Solution**: Always install `accelerate` alongside `transformers` and `datasets`.
```bash
pip install accelerate
```

## Unauthenticated HF Hub Requests
**Problem**: Warning about unauthenticated requests.
**Effect**: Limits download speeds and may cause rate-limiting for large datasets.
**Solution**: For professional work, set a `HF_TOKEN` environment variable or run `huggingface-cli login`. For small experiments, this can usually be ignored.

## Tokenizer Mismatch
**Trap**: Loading a tokenizer from a different model than the classification head.
**Effect**: Results in "unexpected weights" warnings and garbled math.
**Solution**: Always use `AutoTokenizer.from_pretrained(model_name)` matching the base model.


Up: [[Index - Engineering Traps]]
