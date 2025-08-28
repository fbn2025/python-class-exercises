#Class Exercise on Conditionals
# Program to grade exam score

# Ask user for their exam score
score = int(input("Enter your exam score (0–100): "))

# Validate input
if score < 0 or score > 100:
    print("Invalid score! Please enter a number between 0 and 100.")
else:
    # Use conditionals to determine grade
    if score >= 70:
        print("Grade: A")
    elif score >= 60:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    elif score >= 40:
        print("Grade: D")
    else:
        print("Grade: F")
# Print the grade to the user
