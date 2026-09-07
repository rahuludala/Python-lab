# Reverse order of words

s = input("Enter a sentence: ")

words = s.split()
reversed_words = words[::-1]

print("Reversed sentence:", " ".join(reversed_words))
