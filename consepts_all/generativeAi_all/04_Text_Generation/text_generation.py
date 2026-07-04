# Text Generation - How AI generates text
# This file shows the concept using rule-based + template generation
# (No API key needed to learn the concept)

import random

# --- 1. Template-based generation ---
def generate_sentence(subject, verb, obj):
    return f"{subject} {verb} {obj}."

print("=== Template Generation ===")
print(generate_sentence("The robot", "reads", "books"))
print(generate_sentence("Python", "powers", "AI applications"))

# --- 2. Random text generation (Markov-style concept) ---
word_map = {
    "I": ["love", "learn", "use"],
    "love": ["Python", "coding", "AI"],
    "learn": ["Python", "FastAPI", "ML"],
    "Python": ["is", "helps", "runs"],
    "is": ["easy", "powerful", "fun"],
}

def generate_text(start_word, length=5):
    words = [start_word]
    current = start_word
    for _ in range(length - 1):
        next_words = word_map.get(current)
        if not next_words:
            break
        current = random.choice(next_words)
        words.append(current)
    return " ".join(words)

print("\n=== Random Text Generation ===")
for _ in range(3):
    print(generate_text("I"))

# --- 3. How real LLMs generate (concept) ---
print("\n=== How LLMs Generate Text ===")
steps = [
    "1. Tokenize input prompt",
    "2. Pass tokens through transformer layers",
    "3. Predict probability of next token",
    "4. Sample next token (based on temperature)",
    "5. Repeat until max tokens or stop signal",
]
for step in steps:
    print(" ", step)
