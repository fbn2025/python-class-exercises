def grade_score(score):
    if score < 0 or score > 100:
        return "Invalid score - please enter a score between 0 and 100"
    elif score >= 70:
        return "Your grade is A"
    elif score >= 60:
        return "Your grade is B"
    elif score >= 50:
        return "Your grade is C"
    elif score >= 40:
        return "Your grade is D"
    else:
        return "Your grade is F"

try:
    score = int(input("Enter your exam score (0-100): "))
    print(grade_score(score))
except ValueError:
    print("Invalid input - please enter a number")




