import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@timer
def large_sum():
    total = 0

    for i in range(1, 1000001):
        total += i

    return total


result = large_sum()

print("Sum:", result)
