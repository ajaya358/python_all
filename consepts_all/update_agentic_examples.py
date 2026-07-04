from pathlib import Path

root = Path(r'd:\Jayaram\jai\python\consepts_all\agenticAi_all')
files = {
    '01_Intro': 'intro.py',
    '02_Agent_Basics': 'agent_basics.py',
    '03_Tools_And_Actions': 'tools_and_actions.py',
    '04_Memory_And_State': 'memory_and_state.py',
    '05_Workflows': 'workflows.py',
    '06_Reasoning': 'reasoning.py',
    '07_Applications': 'applications.py',
}

content_map = {
    '01_Intro': '''print("Agentic AI intro")\n\nprint("Agentic AI means building systems that can act with some autonomy.")\nprint("A simple agent can observe, decide, and respond.")\n''',
    '02_Agent_Basics': '''print("Agent basics")\n\nclass SimpleAgent:\n    def __init__(self, name):\n        self.name = name\n\n    def respond(self, user_input):\n        if "hello" in user_input.lower():\n            return f"{self.name}: Hi! How can I help you?"\n        if "bye" in user_input.lower():\n            return f"{self.name}: Goodbye!"\n        return f"{self.name}: I can help with simple tasks."\n\nagent = SimpleAgent("Bot")\nprint(agent.respond("hello"))\nprint(agent.respond("bye"))\n''',
    '03_Tools_And_Actions': '''print("Tools and actions")\n\ndef search_web(query):\n    return f"Searching for: {query}"\n\ndef use_tool(tool_name, query):\n    if tool_name == "search":\n        return search_web(query)\n    return "Unknown tool"\n\nprint(use_tool("search", "Python"))\n''',
    '04_Memory_And_State': '''print("Memory and state")\n\nstate = {"conversation_count": 0}\n\ndef remember(user_message):\n    state["conversation_count"] += 1\n    return f"Stored message: {user_message} (count={state['conversation_count']})"\n\nprint(remember("Hello"))\nprint(state)\n''',
    '05_Workflows': '''print("Workflows")\n\ndef run_workflow(task):\n    steps = ["understand task", "plan action", "execute action"]\n    return f"Task: {task} -> Steps: {steps}"\n\nprint(run_workflow("summarize report"))\n''',
    '06_Reasoning': '''print("Reasoning")\n\ndef reason(decision):\n    if decision == "buy":\n        return "Choose the best option based on value"\n    return "Ask for more information"\n\nprint(reason("buy"))\n''',
    '07_Applications': '''print("Applications")\n\ndef build_agent_app(goal):\n    return f"Agent app ready for: {goal}"\n\nprint(build_agent_app("answer questions"))\n''',
}

for folder, filename in files.items():
    path = root / folder / filename
    path.write_text(content_map[folder], encoding='utf-8')

print('Agentic AI examples updated.')
