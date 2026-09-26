import re

def double(m):
    return str(int(m.group()) * 2)

s = "I have 3 apples and 5 oranges"
print(re.sub(r"\d+", double, s))
