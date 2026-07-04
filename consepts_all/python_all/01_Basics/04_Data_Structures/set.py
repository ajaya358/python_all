# Creating a set
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4} → duplicates removed automatically

# add() → add element
numbers.add(5)

# remove() → remove element
numbers.remove(2)

# union() and intersection()
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
