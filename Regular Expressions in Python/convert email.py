import re

s = "Doe, John"
print(re.sub(r"(\w+), (\w+)", r"\2 \1", s))
