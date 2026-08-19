N = 5

for i in range(1, N + 1):
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()
