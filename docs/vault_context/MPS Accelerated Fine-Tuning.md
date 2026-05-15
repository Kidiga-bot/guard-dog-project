---
type: pattern
project: Guard Dog
tags:
  - pytorch
  - mps
  - apple-silicon
  - training
created: 2026-05-15
provenance: 1.0
---

# MPS Accelerated Fine-Tuning

A pattern for training Transformers models efficiently on Apple Silicon (M1/M2/M3/M4/M5) using the PyTorch MPS backend.

## Implementation

### Environment Requirements
To use the `Trainer` with hardware acceleration on Mac, the `accelerate` library is mandatory.
```bash
pip install accelerate
```

### Training Arguments
The `TrainingArguments` class automatically detects the MPS backend if available.
```python
training_args = TrainingArguments(
    output_dir="./model_output",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_steps=10
)
```

### Trainer Setup
```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"]
)
trainer.train()
```

## Benefits
- **Unified Memory**: Allows larger batch sizes than small dedicated VRAM GPUs (e.g., GTX 1650).
- **Efficiency**: Significantly faster than CPU-only training.

## Related
- [[Guard Dog]]
- [[ML Environment Dependencies]]


Up: [[Index - Engineering Patterns]]
