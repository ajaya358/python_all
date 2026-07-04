import json
from urllib.request import urlopen

sample_data = {"name": "Ajay", "age": 21}
print(json.dumps(sample_data, indent=2))

with urlopen("https://jsonplaceholder.typicode.com/todos/1") as response:
    data = json.load(response)
    print("Todo title:", data["title"])
