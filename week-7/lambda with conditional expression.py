grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [35, 45, 67, 28, 80, 39]

for marks in marks_list:
    print(marks, ":", grade(marks))
