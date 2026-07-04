def count_numbers(limit):
    for number in range(limit):
        yield number


for value in count_numbers(5):
    print(value)


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print(list(fibonacci(20)))
