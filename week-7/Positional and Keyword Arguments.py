def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)
    print()

# Positional arguments
student_info("Rahul", "25341A05P4", "CSE")

# Keyword arguments in different order
student_info(branch="CSE", name="Rahul", roll_no="25341A05P4")
