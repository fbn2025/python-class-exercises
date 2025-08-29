# write your if/elif/else statements here
# Ask the user for their exam score
score = int(input("Enter your exam score (0–100): "))

# Determine the grade using conditionals
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
print(f"Your grade is: {grade}")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

