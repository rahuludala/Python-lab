# String to list and list to string

s = input("Enter a string: ")

characters = list(s)

print("List of characters:", characters)

new_string = "".join(characters)

print("String:", new_string)
