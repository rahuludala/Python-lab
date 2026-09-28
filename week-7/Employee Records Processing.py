from functools import reduce

employees = [
    {"name": "Rahul", "department": "CSE", "salary": 40000},
    {"name": "Sita", "department": "ECE", "salary": 35000},
    {"name": "Amit", "department": "CSE", "salary": 45000},
    {"name": "Priya", "department": "CSE", "salary": 50000},
    {"name": "Ravi", "department": "ECE", "salary": 38000}
]

# Select CSE employees
cse_employees = list(
    filter(lambda emp: emp["department"] == "CSE", employees)
)

# Give 10% salary hike without changing original dictionaries
hiked_employees = list(
    map(
        lambda emp: {
            **emp,
            "salary": emp["salary"] * 1.10
        },
        cse_employees
    )
)

# Calculate total salary after hike
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    hiked_employees,
    0
)

print("CSE Employees after 10% hike:")

for emp in hiked_employees:
    print(emp)

print("Total salary expenditure:", total_salary)
