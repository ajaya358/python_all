# Memory and State - Agent remembers past interactions

# --- Short-term Memory (conversation history) ---
print("=== Short-Term Memory (Chat History) ===")

class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "message": message})

    def get_context(self):
        return self.history

    def last_n(self, n=3):
        return self.history[-n:]

memory = ChatMemory()
memory.add("user", "What is Python?")
memory.add("agent", "Python is a programming language.")
memory.add("user", "Is it good for AI?")
memory.add("agent", "Yes, Python is the top language for AI.")

print("Full history:")
for msg in memory.get_context():
    print(f"  {msg['role']}: {msg['message']}")

print("\nLast 2 messages:")
for msg in memory.last_n(2):
    print(f"  {msg['role']}: {msg['message']}")

# --- Long-term Memory (key-value store) ---
print("\n=== Long-Term Memory (Key-Value Store) ===")

class LongTermMemory:
    def __init__(self):
        self.store = {}

    def remember(self, key, value):
        self.store[key] = value
        print(f"  Stored: {key} = {value}")

    def recall(self, key):
        value = self.store.get(key, "Not found")
        print(f"  Recalled: {key} = {value}")
        return value

ltm = LongTermMemory()
ltm.remember("user_name", "Jayaram")
ltm.remember("preferred_language", "Python")
ltm.recall("user_name")
ltm.recall("preferred_language")
ltm.recall("age")  # not stored
