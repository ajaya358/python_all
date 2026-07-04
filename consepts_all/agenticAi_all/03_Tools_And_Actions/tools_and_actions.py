# Tools and Actions - Agent uses tools to complete tasks
# A tool is a function the agent can call (search, calculator, file reader, etc.)

# --- Define Tools ---
def search_web(query):
    # Simulated web search
    results = {
        "python": "Python is a high-level programming language.",
        "fastapi": "FastAPI is a modern Python web framework.",
        "machine learning": "ML is teaching computers to learn from data.",
    }
    return results.get(query.lower(), f"No results found for '{query}'")

def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def get_weather(city):
    # Simulated weather tool
    weather = {"Chennai": "Sunny 35°C", "Mumbai": "Cloudy 28°C", "Delhi": "Windy 22°C"}
    return weather.get(city, "Weather data not available")

# --- Tool Registry ---
tools = {
    "search": search_web,
    "calculator": calculator,
    "weather": get_weather,
}

# --- Agent that picks and uses tools ---
class ToolAgent:
    def __init__(self, tools):
        self.tools = tools

    def use_tool(self, tool_name, input_data):
        if tool_name in self.tools:
            result = self.tools[tool_name](input_data)
            print(f"  Tool: {tool_name} | Input: {input_data} | Result: {result}")
            return result
        print(f"  Tool '{tool_name}' not found")
        return None

agent = ToolAgent(tools)
print("=== Agent Using Tools ===")
agent.use_tool("search", "python")
agent.use_tool("calculator", "10 * 5 + 3")
agent.use_tool("weather", "Chennai")
agent.use_tool("search", "fastapi")
