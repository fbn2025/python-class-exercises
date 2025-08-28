# Class Exercise on Conditionals

# Ask the user for their exam score
score = int(input("Enter your exam score (0–100): "))

# Use conditionals to determine grade
if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"Your score is {score}, so your grade is {grade}.")


