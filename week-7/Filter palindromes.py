def is_palindrome(word):
    return word == word[::-1]


words = ["madam", "hello", "level", "python", "radar", "world"]

palindromes = list(filter(is_palindrome, words))

print("Palindromes:", palindromes)
