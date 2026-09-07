# Count occurrences of a character

s = input("Enter a string: ")
ch = input("Enter the character to count: ")

count = 0

for c in s:
    if c == ch:
        count += 1

print("Occurrences:", count)
