# Prompt Engineering Basics
# A prompt is the instruction you give to an AI model

# --- Prompt Types ---

# 1. Zero-shot: No examples given
zero_shot = "Translate to French: Hello, how are you?"
print("Zero-shot prompt:", zero_shot)

# 2. Few-shot: Give examples before the task
few_shot = """
Translate English to French:
English: Good morning -> French: Bonjour
English: Thank you -> French: Merci
English: How are you? -> French:
"""
print("\nFew-shot prompt:", few_shot)

# 3. Role-based prompt
role_prompt = "You are a Python expert. Explain what a list is in simple terms."
print("Role prompt:", role_prompt)

# 4. Chain of thought: Ask model to reason step by step
cot_prompt = "Solve step by step: If I have 10 apples and give 3 to Ravi, how many do I have?"
print("\nChain of thought prompt:", cot_prompt)

# --- Prompt Tips ---
tips = [
    "Be specific and clear",
    "Give context or role",
    "Use examples (few-shot)",
    "Ask for step-by-step reasoning",
    "Specify output format (JSON, list, etc.)",
]
print("\nPrompt Tips:")
for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")
