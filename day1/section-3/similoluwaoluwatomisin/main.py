# Asks the user for their exam score (0–100).
# Uses conditionals to print their grade
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
