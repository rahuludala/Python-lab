# (a) Square of a number
square = lambda x: x * x

# (b) Check if a number is even
is_even = lambda x: x % 2 == 0

# (c) Larger of two numbers
larger = lambda a, b: a if a > b else b

# Sample inputs
print("Square of 5:", square(5))
print("Is 8 even?", is_even(8))
print("Larger of 15 and 20:", larger(15, 20))
