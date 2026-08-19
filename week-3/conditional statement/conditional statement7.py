year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))

# Check leap year
if year % 400 == 0:
    leap = True
else:
    leap = False

# Number of days in each month
days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

# Adjust February for leap year
if leap:
    days_in_month[1] = 29

# Validate date
if month < 1 or month > 12:
    print("Invalid date")
elif day < 1 or day > days_in_month[month - 1]:
    print("Invalid date")
else:
    print("Valid date")
