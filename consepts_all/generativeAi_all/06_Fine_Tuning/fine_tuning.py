# Fine-Tuning - Adapting a pre-trained model to your specific task
# Pre-trained model (general) → Fine-tune on your data → Specialized model

print("=== What is Fine-Tuning? ===")
print("Base model trained on internet data (general knowledge)")
print("Fine-tune = continue training on YOUR specific dataset")
print("Result: model that understands your domain better\n")

# --- When to fine-tune vs prompt engineering ---
comparison = {
    "Prompt Engineering": "No training needed, fast, good for general tasks",
    "Fine-Tuning": "Needs labeled data, slower, better for specific tasks",
    "RAG (Retrieval)": "No training, adds external knowledge at query time",
}
print("=== Approaches Comparison ===")
for method, desc in comparison.items():
    print(f"  {method}: {desc}")

# --- Fine-tuning steps (concept) ---
print("\n=== Fine-Tuning Steps ===")
steps = [
    "1. Choose a base model (e.g., GPT-2, LLaMA, BERT)",
    "2. Prepare labeled dataset (input → expected output)",
    "3. Format data (prompt-completion pairs)",
    "4. Train with lower learning rate (don't overwrite base knowledge)",
    "5. Evaluate on validation set",
    "6. Deploy fine-tuned model",
]
for step in steps:
    print(f"  {step}")

# --- Sample training data format ---
print("\n=== Sample Training Data Format ===")
training_data = [
    {"prompt": "What is Python?", "completion": "Python is a high-level programming language."},
    {"prompt": "What is FastAPI?", "completion": "FastAPI is a modern web framework for Python."},
    {"prompt": "What is ML?", "completion": "ML is teaching computers to learn from data."},
]
for item in training_data:
    print(f"  Prompt: {item['prompt']}")
    print(f"  Completion: {item['completion']}\n")

# Real fine-tuning: pip install transformers datasets
# from transformers import Trainer, TrainingArguments
