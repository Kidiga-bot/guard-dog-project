#My first self trained model
# Guard Dog: Prompt Injection Detector

A lightweight, high-performance security layer for Large Language Models (LLMs). Trained on `distilbert-base-uncased`, this model acts as a binary classifier to detect and block prompt injection attacks before they reach your primary agent.

## Features
- **Fast Inference**: Small model footprint (<500MB) optimized for local deployment.
- **Hardware Accelerated**: Optimized for Apple Silicon (M-series) using PyTorch MPS.
- **High Confidence**: Binary classification (Safe vs. Malicious) with softmax probability output.

## Project Structure
- `1_load_data.py`: Fetches security datasets from Hugging Face.
- `2_tokenize_data.py`: Demonstrates text-to-tensor conversion.
- `3_prepare_data.py`: Handles padding and truncation for uniform input.
- `4_train_model.py`: Fine-tuning loop for custom security head.
- `5_test_model.py`: Local inference and validation script.

## Setup
```bash
# Create environment
conda create --name guard_dog python=3.11
conda activate guard_dog

# Install dependencies
pip install torch torchvision torchaudio transformers datasets accelerate
```

## Training
To train your own version of the Guard Dog:
```bash
python 4_train_model.py
```

## Testing
To test the model on a real prompt:
```bash
python 5_test_model.py
```

## License
MIT
