'''
| Exception           | Description                        |
| ------------------- | ---------------------------------- |
| `ValueError`        | Invalid value (e.g., `int("abc")`) |
| `ZeroDivisionError` | Divide by zero                     |
| `FileNotFoundError` | File does not exist                |
| `TypeError`         | Wrong data type                    |
| `IndexError`        | List index out of range            |
| `KeyError`          | Dictionary key not found           |
| `NameError`         | Variable not defined               |
'''
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")
