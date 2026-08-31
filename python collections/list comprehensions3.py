# Create a list of words with more than 4 letters

words = ["apple", "cat", "banana", "dog", "orange", "book", "computer"]
long_words = [word for word in words if len(word) > 4]
print("Original list:", words)
print("Words with more than 4 letters:", long_words)
