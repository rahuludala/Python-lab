# lab1_task4.py

def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


# Input numbers
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

# Unpack returned tuple
minimum, maximum, average = stats(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)
