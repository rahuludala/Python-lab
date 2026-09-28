import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper


@log_call
@timer
def add(a, b):
    return a + b


result = add(10, 20)
