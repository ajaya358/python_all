# Generative AI - Introduction
# Generative AI creates new content: text, images, code, audio
# Key models: GPT (text), DALL-E (images), Codex (code)

# Core concepts
concepts = {
    "LLM": "Large Language Model - trained on huge text data",
    "Prompt": "Input text you give to the model",
    "Token": "Smallest unit of text the model processes",
    "Temperature": "Controls randomness (0=focused, 1=creative)",
    "Context Window": "Max tokens the model can process at once",
}

for term, definition in concepts.items():
    print(f"{term}: {definition}")

# Simple rule-based text generation (no API needed)
def simple_generate(topic):
    templates = {
        "weather": "Today the weather is sunny and warm.",
        "food": "Pizza is a popular dish made with dough and toppings.",
        "python": "Python is a simple and powerful programming language.",
    }
    return templates.get(topic.lower(), f"I don't have info about '{topic}' yet.")

print("\n--- Simple Generator ---")
print(simple_generate("python"))
print(simple_generate("weather"))
