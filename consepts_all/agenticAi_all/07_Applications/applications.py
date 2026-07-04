# Agentic AI Applications - Full mini agent combining all concepts

print("=== Mini AI Agent Application ===\n")

# Tools
def search(query):
    db = {
        "python": "Python is a high-level programming language used in AI, web, and data.",
        "fastapi": "FastAPI is a fast Python web framework for building APIs.",
        "ml": "Machine Learning is teaching computers to learn from data.",
    }
    return db.get(query.lower(), f"No info found for '{query}'")

def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Invalid expression"

def summarize(text):
    words = text.split()
    return " ".join(words[:10]) + "..." if len(words) > 10 else text

# Memory
class AgentMemory:
    def __init__(self):
        self.history = []

    def save(self, role, msg):
        self.history.append(f"{role}: {msg}")

    def show(self):
        print("\n--- Conversation History ---")
        for h in self.history:
            print(f"  {h}")

# Full Agent
class FullAgent:
    def __init__(self, name):
        self.name = name
        self.memory = AgentMemory()
        self.tools = {"search": search, "calculate": calculate, "summarize": summarize}

    def think(self, user_input):
        if any(op in user_input for op in ["+", "-", "*", "/"]):
            return "calculate", user_input
        if "summarize" in user_input.lower():
            return "summarize", user_input.replace("summarize", "").strip()
        return "search", user_input.strip()

    def respond(self, user_input):
        self.memory.save("User", user_input)
        tool_name, tool_input = self.think(user_input)
        result = self.tools[tool_name](tool_input)
        response = f"[{tool_name}] {result}"
        self.memory.save(self.name, response)
        print(f"  User: {user_input}")
        print(f"  {self.name}: {response}\n")

agent = FullAgent("AgentBot")
agent.respond("python")
agent.respond("100 * 5 + 50")
agent.respond("fastapi")
agent.respond("summarize Python is great for AI and web development and data science")
agent.memory.show()
