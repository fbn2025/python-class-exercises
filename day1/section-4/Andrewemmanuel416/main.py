# Program to determine grade based on exam score

try:
    # Ask the user for their exam score
    score = int(input("Enter your exam score (0-100): "))

    # Validate input range
    if score < 0 or score > 100:
        print("Invalid score! Please enter a number between 0 and 100.")
    else:
        # Check the grade using if/elif/else
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

except ValueError:
    print("Invalid input! Please enter a numeric value between 0 and 100.")
