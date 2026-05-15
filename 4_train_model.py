from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

def train_guard_dog():
    print("1. Loading data and tokenizer...")
    dataset = load_dataset("deepset/prompt-injections")
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    print("2. Tokenizing data...")
    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    print("3. Loading the Base Model...")
    #  load the base model proviving details of dataset (Safe or Malicious)
    model = AutoModelForSequenceClassification.from_pretrained(
        "distilbert-base-uncased", 
        num_labels=2
    )

    print("4. Setting up training parameters...")
    # These are the "rules" for how the AI should learn
    training_args = TrainingArguments(
        output_dir="./guard_dog_saved_model",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        num_train_epochs=2, # We will read the dataset 2 times
        weight_decay=0.01,
        logging_steps=10
    )

    print("5. Initializing the Trainer...")
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"]
    )

    print("6. STARTING TRAINING! ( M5 chip is taking over now...)")
    trainer.train()

    print("7. Training Complete! Saving  new custom AI to your hard drive...")
    trainer.save_model("./guard_dog_saved_model")
    tokenizer.save_pretrained("./guard_dog_saved_model")
    
    print("Success! custom model is saved in the 'guard_dog_saved_model' folder.")

if __name__ == "__main__":
    train_guard_dog()
