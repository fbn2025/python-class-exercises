score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here

if score >= 70:
    print("A")
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"
# Print the result
print(f"Your grade is: {grade}")
