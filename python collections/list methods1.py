# Demonstrate different list methods

numbers = [5, 2, 8, 3, 2]

print("Original list:", numbers)

# append()
numbers.append(10)
print("After append(10):", numbers)

# insert()
numbers.insert(2, 7)
print("After insert(2, 7):", numbers)

# extend()
numbers.extend([12, 15])
print("After extend([12, 15]):", numbers)

# remove()
numbers.remove(2)
print("After remove(2):", numbers)

# pop()
numbers.pop()
print("After pop():", numbers)

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# count()
print("Count of 2:", numbers.count(2))
print("List after count():", numbers)

# index()
print("Index of 8:", numbers.index(8))
print("List after index():", numbers)
