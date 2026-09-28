def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


def reverse_number(n):
    def reverse_helper(n, rev):
        if n == 0:
            return rev
        return reverse_helper(n // 10, rev * 10 + n % 10)

    return reverse_helper(n, 0)


n = int(input("Enter a positive integer: "))

print("Sum of digits:", sum_of_digits(n))
print("Reversed number:", reverse_number(n))
