# accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

# account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

#Overwritten with if/elif/else code based for exam score check
score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here
if score >= 101:
    print("Scores are between 0-100")
elif score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")
