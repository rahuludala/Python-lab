# lab1_task3.py

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Driver program
for i in range(5):
    num = int(input("Enter a number: "))

    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")
