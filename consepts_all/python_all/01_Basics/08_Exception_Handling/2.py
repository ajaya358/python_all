'''
| Block            | Purpose                           |
| ---------------- | --------------------------------- |
| `try`            | Code that may cause error         |
| `except`         | Handle specific or general errors |
| `else`           | Runs if no exception occurs       |
| `finally`        | Always runs (cleanup)             |
| `raise`          | Manually throw an error           |
| Custom Exception | Define your own error class       |
'''
try:
    a = int("abc")
    b = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

