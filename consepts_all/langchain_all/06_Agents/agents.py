# LangChain Agents - LLM decides which tool to use
# pip install langchain langchain-openai

print("=== What is a LangChain Agent? ===")
print("  Agent = LLM + Tools + ReAct loop")
print("  LLM reads question → decides which tool to call → uses result → answers\n")

print("=== Agent Types ===")
agent_types = {
    "ReAct":            "Reason + Act — think step by step, use tools",
    "OpenAI Functions": "Uses OpenAI function calling — most reliable",
    "Tool Calling":     "Modern standard — works with many LLMs",
    "Conversational":   "Agent with memory for chat",
}
for k, v in agent_types.items():
    print(f"  {k:22}: {v}")

# --- Manual agent simulation (no API key needed) ---
print("\n=== Manual Agent Simulation ===")

def search_tool(query):
    db = {
        "python":    "Python is a programming language created by Guido van Rossum.",
        "fastapi":   "FastAPI is a Python web framework by Sebastián Ramírez.",
        "langchain": "LangChain is a framework for building LLM applications.",
    }
    return db.get(query.lower(), f"No info found for '{query}'")

def calculator_tool(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

def weather_tool(city):
    return f"Weather in {city}: Sunny, 32°C"

tools = {
    "search":     search_tool,
    "calculator": calculator_tool,
    "weather":    weather_tool,
}

class SimpleAgent:
    def __init__(self, tools):
        self.tools = tools

    def decide_tool(self, question):
        q = question.lower()
        if "weather" in q:
            return "weather", q.split("in")[-1].strip().strip("?")
        if any(c.isdigit() for c in q) and any(op in q for op in ["+", "-", "*", "/"]):
            import re
            expr = re.search(r"[\d\s\+\-\*\/\.]+", q)
            return "calculator", expr.group().strip() if expr else "0"
        return "search", q.split()[-1].strip("?")

    def run(self, question):
        print(f"  Question: {question}")
        tool_name, tool_input = self.decide_tool(question)
        print(f"  Thought:  Use '{tool_name}' tool")
        result = self.tools[tool_name](tool_input)
        print(f"  Action:   {tool_name}('{tool_input}')")
        print(f"  Answer:   {result}\n")

agent = SimpleAgent(tools)
agent.run("Tell me about Python")
agent.run("What is the weather in Chennai?")
agent.run("Calculate 150 * 12")

print("=== Real LangChain Agent Code ===")
print("""
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate

@tool
def search(query: str) -> str:
    \"\"\"Search for information about a topic\"\"\"
    return f"Result for: {query}"

llm = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
agent = create_tool_calling_agent(llm, [search], prompt)
executor = AgentExecutor(agent=agent, tools=[search], verbose=True)
executor.invoke({"input": "Tell me about Python"})
""")
