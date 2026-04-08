# Writing a list of items
data = ["Python", "FastAPI", "MongoDB"]

with open("topics.txt", "w") as f:
    for item in data:
        f.write(item + "\n")

# Reading them back
with open("topics.txt", "r") as f:
    items = f.readlines()

print(items)  # ['Python\n', 'FastAPI\n', 'MongoDB\n']
