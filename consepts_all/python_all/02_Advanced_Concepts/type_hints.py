from typing import List, Dict


def add_numbers(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


def build_profile(name: str, age: int) -> Dict[str, int | str]:
    return {"name": name, "age": age}


print(add_numbers(3, 5))
print(greet("Python"))
print(build_profile("Ajay", 21))
