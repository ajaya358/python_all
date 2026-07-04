class MyRange:
    def __init__(self, end):
        self.end = end
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for value in MyRange(4):
    print(value)

# List comprehension
squares = [x * x for x in range(6)]
print("Squares:", squares)

# Dictionary comprehension
square_map = {x: x * x for x in range(5)}
print("Square map:", square_map)
