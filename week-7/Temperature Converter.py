# lab1_task5.py

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


# Menu-driven program
while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit =", f)

    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print("Temperature in Celsius =", c)

    elif choice == 3:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
