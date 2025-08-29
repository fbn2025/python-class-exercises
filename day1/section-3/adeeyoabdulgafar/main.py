# Class Exercise on Conditionals

# ## Class Exercise on Conditionals

# Task: Write a program that:
# Asks the user for their exam score (0–100).
# Uses conditionals to print their grade:

# 70 and above → "A"
# 60–69 → "B"
# 50–59 → "C"
# 40–49 → "D"
# below 40 → "F"

# Goal: To help you learn how to branch logic with if/elif/else.




Exam_Score = int(input("Enter your Exam Score: "))
Pecfect_Score = 100


# if/elif/else chain
if Exam_Score < 40:
    print("F")
elif Exam_Score <= 49:
    print("D")
elif Exam_Score <= 59:
    print("C")
elif Exam_Score <= 69:
    print("B")
elif Exam_Score < 100:
    print("A")
elif Exam_Score == Pecfect_Score:
    print("A - Perfect 👏")
else:
    print("Missing script, see the your class teacher")

