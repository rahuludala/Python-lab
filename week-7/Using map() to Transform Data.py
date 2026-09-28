def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(celsius_to_fahrenheit, celsius))

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
