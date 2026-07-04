class Agent:
    def __init__(self, name):
        self.name = name

    def think(self, task):
        return f"{self.name} is planning how to complete: {task}"

    def act(self, task):
        return f"{self.name} is executing: {task}"


agent = Agent("AI Agent")
print(agent.think("write a report"))
print(agent.act("write a report"))
