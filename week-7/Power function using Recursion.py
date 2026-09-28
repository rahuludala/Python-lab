def power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1 / power(base, -exp)


base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result:", power(base, exp))
