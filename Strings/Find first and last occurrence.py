# Find first and last occurrence

s = input("Enter a string: ")
ch = input("Enter a character: ")

first = s.find(ch)
last = s.rfind(ch)

if first != -1:
    print("First occurrence index:", first)
    print("Last occurrence index:", last)
else:
    print("Character not found")
