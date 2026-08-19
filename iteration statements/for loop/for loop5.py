lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Prime numbers are:")

for num in range(lower, upper + 1):
    if num < 2:
        continue

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
