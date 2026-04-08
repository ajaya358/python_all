'''
| Operator | Meaning           | Example                  |
| -------- | ----------------- | ------------------------ |
| `and`    | True if both true | `True and False → False` |
| `or`     | True if one true  | `True or False → True`   |
| `not`    | Negates value     | `not True → False`       |
'''
x = 5
y = 3

print(x > 2 and y < 5)  # True
print(x > 2 or y > 5)   # True
print(not(x > 2))       # False
