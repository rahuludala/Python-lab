# Replace negative numbers with 0 using list comprehension

numbers = [10, -5, 20, -8, 15, -3, 7]
result = [0 if num < 0 else num for num in numbers]
print("Original list:", numbers)
print("Modified list:", result)
