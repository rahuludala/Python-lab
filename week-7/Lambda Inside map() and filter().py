numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cubes using map()
cubes = list(map(lambda x: x ** 3, numbers))

# Numbers divisible by 3 using filter()
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Original numbers:", numbers)
print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible_by_3)
