N = 4

# Upper half
for i in range(1, N + 1):
    spaces = " " * (N - i)
    stars = "* " * i
    print(spaces + stars)

# Lower half
for i in range(N - 1, 0, -1):
    spaces = " " * (N - i)
    stars = "* " * i
    print(spaces + stars)
