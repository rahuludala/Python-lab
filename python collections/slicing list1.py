#Given a list of 10 numbers, print the first 3 elements, the last 3 elements, and every alternate element using slicing

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Every alternate element:", numbers[::2])
