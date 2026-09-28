# lab1_task2.py

def simple_interest(principal, rate, time):
    """Calculate and return the simple interest."""
    si = (principal * rate * time) / 100
    return si


# Get values from the user
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)
