# Function definition ------------------1
def add_numbers(a, b):
    return a + b

# Function call
result = add_numbers(5, 3)
print(result)  # 8


# Default argument-----------------2
def greet(name="Guest"):
    print("Hello,", name)

greet("Jayaram")   # Hello, Jayaram
greet()            # Hello, Guest

# Keyword arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=25, name="Ravi")
# Name: Ravi, Age: 25



