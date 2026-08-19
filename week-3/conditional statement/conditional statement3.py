# Program to check the type of triangle

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Check if the triangle is valid
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle.")
elif a == b == c:
    print("Equilateral triangle.")
elif a == b or b == c or a == c:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")
