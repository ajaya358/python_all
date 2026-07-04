# Reasoning - Agent thinks step by step before acting
# Key pattern: ReAct = Reason + Act

print("=== Types of Reasoning ===")
types = {
    "Rule-based": "If condition → then action (simple, fast)",
    "Chain of Thought": "Think step by step before answering",
    "ReAct": "Reason → Act → Observe → Repeat",
    "Tree of Thought": "Explore multiple reasoning paths, pick best",
}
for k, v in types.items():
    print(f"  {k}: {v}")

# --- Chain of Thought Example ---
print("\n=== Chain of Thought Reasoning ===")

def solve_with_cot(problem):
    print(f"  Problem: {problem}")
    print("  Step 1: Understand what is being asked")
    print("  Step 2: Break into smaller parts")
    print("  Step 3: Solve each part")
    print("  Step 4: Combine for final answer")

solve_with_cot("If I earn 500/day and work 20 days, what is monthly income?")
print("  Answer: 500 × 20 = 10,000")

# --- ReAct Pattern ---
print("\n=== ReAct Pattern ===")

class ReActAgent:
    def __init__(self):
        self.tools = {
            "calculate": lambda x: eval(x),
            "lookup": lambda x: f"Info about '{x}': It is a key concept in AI.",
        }

    def run(self, task):
        print(f"  Task: {task}")
        # Reason
        print("  Thought: I need to calculate the answer")
        # Act
        action, input_data = "calculate", "500 * 20"
        print(f"  Action: {action}({input_data})")
        # Observe
        result = self.tools[action](input_data)
        print(f"  Observation: {result}")
        # Final answer
        print(f"  Final Answer: {result}")

agent = ReActAgent()
agent.run("What is 500 multiplied by 20?")
