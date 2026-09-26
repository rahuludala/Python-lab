import re

text = "NASA and USA visited Hyderabad University"

# Capital words
a = re.findall(r"\b[A-Z]{2,}\b", text)
print(a)

# Words longer than 6 characters
for m in re.finditer(r"\b\w{7,}\b", text):
    print(m.group(), m.start())

# Prices
p = "apples: $3.50, bananas: $1.20, mango: $4.75"
prices = re.findall(r"\$\d+\.\d+", p)
print(prices)
print("Count:", len(prices))
