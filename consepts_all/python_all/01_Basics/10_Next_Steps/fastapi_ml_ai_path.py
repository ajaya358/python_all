# This file is a roadmap-style example showing how Python basics connect to advanced fields.

# 1. Python basics -> FastAPI
# FastAPI uses Python functions and type hints to build APIs.
from typing import List


def greet(name: str) -> str:
    return f"Hello {name}"


# 2. Python basics -> Machine Learning
# Data is stored in lists and dictionaries, then processed with libraries like NumPy and pandas.

def average(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0


# 3. Python basics -> AI
# AI projects often use classes, functions, and data structures to organize logic.
class AIModel:
    def __init__(self, name: str):
        self.name = name

    def predict(self, input_value: int) -> int:
        return input_value * 2


print(greet("Ajay"))
print(average([10, 20, 30]))
model = AIModel("SimpleModel")
print(model.predict(5))
