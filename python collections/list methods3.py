# Find maximum, minimum, and sum without using built-in functions

numbers = [10, 25, 5, 40, 15, 30]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    total += num

print("List:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
