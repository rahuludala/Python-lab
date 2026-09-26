import re

def check_password(pw):
    fail = []

    if len(pw) < 8:
        fail.append("8 characters")
    if not re.search(r"[A-Z]", pw):
        fail.append("uppercase")
    if not re.search(r"[a-z]", pw):
        fail.append("lowercase")
    if not re.search(r"\d", pw):
        fail.append("digit")
    if not re.search(r"[!@#$%^&*]", pw):
        fail.append("symbol")

    return fail

print(check_password("Hello123!"))
print(check_password("hello"))
