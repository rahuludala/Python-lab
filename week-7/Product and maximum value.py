from functools import reduce

numbers = [2, 4, 6, 8, 10]

# Product
product = reduce(lambda a, b: a * b, numbers)

# Maximum without using max()
maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Numbers:", numbers)
print("Product:", product)
print("Maximum:", maximum)
