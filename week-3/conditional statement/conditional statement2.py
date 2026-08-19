# Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year: "))
if (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
