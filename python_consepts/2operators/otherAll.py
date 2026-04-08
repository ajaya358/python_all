'''
f) Membership Operators
| Operator | Meaning                 | Example                     |
| -------- | ----------------------- | --------------------------- |
| `in`     | True if in sequence     | `'a' in 'apple' → True`     |
| `not in` | True if not in sequence | `'b' not in 'apple' → True` |
'''
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)  # True
print("grape" not in fruits)  # True

'''
| Operator | Meaning                                 | Example      |
| -------- | --------------------------------------- | ------------ |
| `is`     | True if both refer to same object       | `x is y`     |
| `is not` | True if they refer to different objects | `x is not y` |
'''
print('Identity Operators')

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      # True
print(x is y)      # False
print(x == y)      # True (values equal)

print('Program Using Operators')
x = 10
y = 3

print(x + y)       # Arithmetic
print(x > y)       # Comparison
print(x > 5 and y < 5) # Logical
x += 2             # Assignment
print(x)
print(x & y)       # Bitwise
print("a" in "apple") # Membership
print(x is y)      # Identity


