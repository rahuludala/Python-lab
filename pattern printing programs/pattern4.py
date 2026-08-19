N = 5

for i in range(N, 0, -1):
    spaces = " " * (N - i)
    stars = "* " * i
    print(spaces + stars)
