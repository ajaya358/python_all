# Generative AI Applications
# Real-world apps built using generative AI concepts

# --- App 1: Simple Chatbot (rule-based, no API) ---
print("=== App 1: Simple Chatbot ===")

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi! How can I help you?",
            "bye": "Goodbye! Have a great day!",
            "help": "I can answer basic questions. Try: hello, bye, name, python",
            "name": "I am GenBot, your AI assistant.",
            "python": "Python is a great language for AI and web development!",
        }

    def chat(self, user_input):
        key = user_input.lower().strip()
        return self.responses.get(key, "I don't understand that yet. Type 'help'.")

bot = SimpleChatbot()
test_inputs = ["hello", "python", "name", "bye"]
for msg in test_inputs:
    print(f"  You: {msg}")
    print(f"  Bot: {bot.chat(msg)}\n")

# --- App 2: Text Summarizer (rule-based) ---
print("=== App 2: Simple Summarizer ===")

def summarize(text, max_sentences=2):
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences]) + "."

article = "Python is a programming language. It is used for AI and web. Many companies use Python. It is easy to learn."
print("Original:", article)
print("Summary:", summarize(article))

# --- App 3: Content Generator ---
print("\n=== App 3: Blog Title Generator ===")

def generate_title(topic):
    templates = [
        f"Top 5 Ways to Learn {topic}",
        f"A Beginner's Guide to {topic}",
        f"Why {topic} is the Future",
        f"How to Master {topic} in 30 Days",
    ]
    import random
    return random.choice(templates)

topics = ["Python", "Machine Learning", "FastAPI"]
for topic in topics:
    print(f"  {topic}: {generate_title(topic)}")
