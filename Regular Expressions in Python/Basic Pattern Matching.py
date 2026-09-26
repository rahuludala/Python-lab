import re

s = "1024 requests were served in 3 seconds"

print(bool(re.match(r"\d", s)))

m = re.search(r"served", s)
print(m.span())

print(bool(re.fullmatch(r"\d+", "12345")))
print(bool(re.fullmatch(r"\d+", "123a5")))
