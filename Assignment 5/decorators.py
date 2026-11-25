from functools import wraps


def trace(tag):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f"[{tag}] args={args}")
            result = func(*args, **kwargs)
            print(f"[{tag}] result={result}")
            print()
            return result
        return inner
    return outer


@trace("add")
def add(x, y):
    return x + y


@trace("multiply")
def multiply(x, y):
    return x * y


add(2, 2)
add(67, 2)
add(34, 35)
add(99, 1)

multiply(3, 7)
multiply(10, 10)
