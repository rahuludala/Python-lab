import re

text = "555-123-4567, (555) 123-4567, 555.123.4567"

p = r"(?:\(\d{3}\)|\d{3})[-. ]\d{3}[-.]\d{4}"

nums = re.findall(p, text)

for n in nums:
    n = re.sub(r"\D", "", n)
    print(n[:3] + "-" + n[3:6] + "-" + n[6:])
