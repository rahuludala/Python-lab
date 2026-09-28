from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greeting():
    print("Hello! Welcome to Python.")


greeting()
