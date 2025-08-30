# Class Exercise on Conditionals

# Task: Write a program that:
# Asks the user for their exam score (0–100).
# Uses conditionals to print their grade:

# 70 and above → "A"
# 60–69 → "B"
# 50–59 → "C"
# 40–49 → "D"
# below 40 → "F"

# Goal: To help you learn how to branch logic with if/elif/else.

# collect student input
score = int(input("Enter your exam score (0-100): "))
if score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")





