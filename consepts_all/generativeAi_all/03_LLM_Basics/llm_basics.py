# LLM Basics - Large Language Models

# Key concepts
print("=== LLM Key Concepts ===")

concepts = {
    "Parameters": "Weights learned during training (GPT-4 has ~1 trillion)",
    "Tokens": "Words/subwords the model reads. 'Hello world' = 2 tokens",
    "Context Window": "Max tokens in one conversation (e.g., 4096, 128k)",
    "Temperature": "0 = deterministic, 1 = creative/random",
    "Top-p (nucleus)": "Controls diversity of word choices",
    "Fine-tuning": "Training a base model on your specific data",
    "Inference": "Using the trained model to generate output",
}

for k, v in concepts.items():
    print(f"  {k}: {v}")

# Token counting simulation
def count_tokens(text):
    # Simple approximation: 1 token ≈ 4 characters
    return max(1, len(text) // 4)

texts = ["Hello", "How are you?", "Python is a great programming language."]
print("\n=== Token Count Estimates ===")
for t in texts:
    print(f"  '{t}' → ~{count_tokens(t)} tokens")

# Popular LLMs
print("\n=== Popular LLMs ===")
llms = [
    ("GPT-4", "OpenAI", "Text, code, reasoning"),
    ("Gemini", "Google", "Text, images, multimodal"),
    ("Claude", "Anthropic", "Long context, safe AI"),
    ("LLaMA", "Meta", "Open source, local use"),
]
for name, company, use in llms:
    print(f"  {name} ({company}): {use}")
