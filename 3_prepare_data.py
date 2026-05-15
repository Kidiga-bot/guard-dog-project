from datasets import load_dataset
from transformers import AutoTokenizer

def prepare_dataset():
    print("Loading dataset and tokenizer...")
    dataset = load_dataset("deepset/prompt-injections")
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

    # We create a function that knows exactly how to format our text
    def tokenize_function(examples):
        # We tell it to pad short sentences and chop long ones
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    print("Tokenizing the entire dataset. This might take a few seconds...")
    
    # The 'map' function efficiently applies our rules to all 500+ examples at once
    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    print("\nDataset successfully converted to numbers!")
    print(f"New data features: {tokenized_datasets['train'].column_names}")
    
    # Let's peek at the actual math array for the first prompt
    print("\n--- The Input IDs for Prompt #1 ---")
    
    # We will just print the first 50 numbers so it doesn't flood your screen
    first_prompt_numbers = tokenized_datasets['train'][0]['input_ids'][:50]
    print(first_prompt_numbers)

if __name__ == "__main__":
    prepare_dataset()