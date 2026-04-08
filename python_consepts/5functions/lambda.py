# Syntax: lambda arguments : expression

square = lambda x: x ** 2
print(square(5))   # 25

add = lambda a, b: a + b
print(add(10, 15))  # 25


# Factorial example ----------------------------------------
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

