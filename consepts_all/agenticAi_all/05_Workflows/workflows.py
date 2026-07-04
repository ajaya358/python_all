# Workflows - Agent follows a sequence of steps to complete a task
# A workflow = ordered list of steps/tasks the agent executes

print("=== What is a Workflow? ===")
print("Workflow = Step 1 → Step 2 → Step 3 → ... → Goal\n")

# --- Simple Sequential Workflow ---
class WorkflowStep:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def run(self, data):
        print(f"  Running step: {self.name}")
        return self.action(data)

class Workflow:
    def __init__(self, name):
        self.name = name
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def execute(self, initial_data):
        print(f"=== Workflow: {self.name} ===")
        data = initial_data
        for step in self.steps:
            data = step.run(data)
        print(f"  Final result: {data}")
        return data

# --- Example: Data Processing Workflow ---
def collect(data):
    return data + ["collected_data"]

def clean(data):
    return [item for item in data if item != "bad_data"]

def analyze(data):
    return {"items": data, "count": len(data)}

def report(data):
    return f"Report: {data['count']} items processed → {data['items']}"

wf = Workflow("Data Pipeline")
wf.add_step(WorkflowStep("Collect", collect))
wf.add_step(WorkflowStep("Clean", clean))
wf.add_step(WorkflowStep("Analyze", analyze))
wf.add_step(WorkflowStep("Report", report))

wf.execute(["item1", "bad_data", "item2"])
