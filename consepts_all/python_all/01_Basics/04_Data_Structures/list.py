# Creating a list
fruits = ["apple", "banana", "cherry"]

# append() → add single item
fruits.append("orange")
print(fruits)   # ['apple', 'banana', 'cherry', 'orange']

# extend() → add multiple items
fruits.extend(["grape", "mango"])
print(fruits)   # ['apple', 'banana', 'cherry', 'orange', 'grape', 'mango']

# remove() → remove specific item
fruits.remove("banana")
print(fruits)   # ['apple', 'cherry', 'orange', 'grape', 'mango']

# pop() → remove by index (default last)
fruits.pop()
print(fruits)   # ['apple', 'cherry', 'orange', 'grape']

# slicing
print(fruits[1:3])  # ['cherry', 'orange']
