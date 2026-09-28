from functools import wraps

is_logged_in = False


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login first.")

    return wrapper


@require_login
def view_profile():
    print("Welcome to your profile!")


# Case 1: Not logged in
print("When user is logged out:")
view_profile()


# Case 2: Logged in
is_logged_in = True

print("\nWhen user is logged in:")
view_profile()
