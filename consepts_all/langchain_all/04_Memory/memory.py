# LangChain Memory - Remember conversation history
# pip install langchain langchain-openai

print("=== Why Memory? ===")
print("  LLMs are stateless — they forget previous messages")
print("  Memory stores chat history and passes it with each new message\n")

print("=== Memory Types ===")
memory_types = {
    "ConversationBufferMemory":        "Stores full conversation history",
    "ConversationBufferWindowMemory":  "Stores last N messages only",
    "ConversationSummaryMemory":       "Summarizes old messages to save tokens",
    "ConversationTokenBufferMemory":   "Keeps messages within token limit",
    "VectorStoreRetrieverMemory":      "Stores in vector DB, retrieves relevant past messages",
}
for k, v in memory_types.items():
    print(f"  {k:40}: {v}")

# --- Manual memory simulation ---
print("\n=== Manual Conversation Memory ===")

class ConversationMemory:
    def __init__(self, window=None):
        self.history = []
        self.window = window  # None = keep all, int = keep last N

    def add(self, role: str, message: str):
        self.history.append({"role": role, "content": message})
        if self.window:
            self.history = self.history[-self.window * 2:]

    def get_context(self) -> str:
        return "\n".join([f"{m['role']}: {m['content']}" for m in self.history])

    def clear(self):
        self.history = []

memory = ConversationMemory(window=3)
memory.add("user", "What is Python?")
memory.add("assistant", "Python is a programming language.")
memory.add("user", "Is it good for AI?")
memory.add("assistant", "Yes, Python is the top language for AI.")
memory.add("user", "What libraries should I learn?")

print("Context passed to LLM:")
print(memory.get_context())

print("\n=== Real LangChain Memory Code ===")
code = """
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

conversation.predict(input="Hi, my name is Ajay")
conversation.predict(input="What is my name?")  # LLM remembers: Ajay
"""
print(code)
