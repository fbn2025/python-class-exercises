
score = int(input("Enter your exam score (0 – 100): "))

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
    
print(f"Your grade is: {grade}")


