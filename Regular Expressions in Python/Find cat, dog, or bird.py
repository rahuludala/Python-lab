import re

s = "I have a cat, dog and bird"
print(re.findall(r"\b(cat|dog|bird)\b", s))
