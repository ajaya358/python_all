def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase
def greet(name):
    return f"hello {name}"


print(greet("ajay"))


def repeat(times):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * times

        return inner

    return decorator


@repeat(3)
def message():
    return "python "


print(message())
