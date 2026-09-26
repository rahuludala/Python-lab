import re

def valid_email(s):
    p = r"^[\w.]+@[\w.]+\.[A-Za-z]{2,6}$"
    return bool(re.fullmatch(p, s))

emails = [
    "john@gmail.com",
    "abc@yahoo.in",
    "user.name@test.com",
    "a@b.com",
    "a@b.c",
    "no-at-sign.com",
    "abc@.com",
    "@gmail.com"
]

for e in emails:
    print(e, valid_email(e))
