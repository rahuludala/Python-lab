students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]

sorted_students = sorted(
    students,
    key=lambda s: s[1],
    reverse=True
)

print("Students sorted by marks:")

for student in sorted_students:
    print(student)
