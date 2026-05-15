#Training a small model on identifying  prompt injection to non prompt injection
from datasets import load_dataset

def explore_data():
    print("Downloading the dataset from Hugging Face...")
    # This pulls the data directly into your Mac's memory
    dataset = load_dataset("deepset/prompt-injections")
    
    print("\n Dataset loaded successfully!")
    print(f"Total training examples available: {len(dataset['train'])}")
    
    print("\n --- Inspecting the Data ---")
    
    # We grab the first item (index 0) which is a safe prompt
    safe_example = dataset['train'][0]
    print(f"\n[SAFE] Label {safe_example['label']}:")
    print(f"\"{safe_example['text']}\"")
    
    # We grab an item further down (index 45) which is a malicious injection
    injection_example = dataset['train'][45]
    print(f"\n[MALICIOUS] Label {injection_example['label']}:")
    print(f"\"{injection_example['text']}\"")

if __name__ == "__main__":
    explore_data()