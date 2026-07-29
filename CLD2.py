import sys

if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum =", a + b)
else:
    print("Usage: python file.py num1 num2")
