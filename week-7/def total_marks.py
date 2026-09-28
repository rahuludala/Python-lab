def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# 3 marks
total, average = total_marks(80, 75, 90)
print("3 Marks -> Total:", total, "Average:", average)

# 5 marks
total, average = total_marks(80, 75, 90, 85, 70)
print("5 Marks -> Total:", total, "Average:", average)

# 1 mark
total, average = total_marks(95)
print("1 Mark -> Total:", total, "Average:", average)
