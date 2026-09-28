def to_upper(text):
    return text.upper()


words = ["python", "java", "c", "programming"]

result = list(map(to_upper, words))

print("Original:", words)
print("Uppercase:", result)
