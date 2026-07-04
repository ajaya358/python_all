print("Agent basics")

class SimpleAgent:
    def __init__(self, name):
        self.name = name

    def respond(self, user_input):
        if "hello" in user_input.lower():
            return f"{self.name}: Hi! How can I help you?"
        if "bye" in user_input.lower():
            return f"{self.name}: Goodbye!"
        return f"{self.name}: I can help with simple tasks."

agent = SimpleAgent("Bot")
print(agent.respond("hello"))
print(agent.respond("bye"))
