# Agentic AI - Introduction
# An AI Agent perceives → thinks → acts → repeats (loop)

print("=== What is Agentic AI? ===")
concepts = {
    "Agent": "AI that takes actions to achieve a goal autonomously",
    "Perception": "Agent reads input (user message, tool output, environment)",
    "Reasoning": "Agent decides what to do next",
    "Action": "Agent calls a tool, writes code, searches web, etc.",
    "Memory": "Agent remembers past steps to make better decisions",
    "Loop": "Agent keeps acting until goal is reached",
}
for k, v in concepts.items():
    print(f"  {k}: {v}")

# --- Simple Agent Loop (concept) ---
print("\n=== Agent Loop Example ===")

class BasicAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.steps = []

    def perceive(self, observation):
        print(f"  [{self.name}] Observed: {observation}")
        self.steps.append(observation)

    def think(self):
        if len(self.steps) < 2:
            return "gather_more_info"
        return "complete_task"

    def act(self, action):
        print(f"  [{self.name}] Action: {action}")

    def run(self, observations):
        print(f"\nGoal: {self.goal}")
        for obs in observations:
            self.perceive(obs)
            decision = self.think()
            self.act(decision)

agent = BasicAgent("ResearchBot", "Find info about Python")
agent.run(["User asked about Python", "Found Python docs online"])
