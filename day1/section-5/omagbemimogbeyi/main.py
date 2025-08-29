Exercise 1
# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

user_account = input("Enter an account number: ")

found = False
for account in accounts:
    if user_account == account:
        found = True
        break

if found:
    print("200 - Account found")
else:
    print("404 - Account not found")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

Exercise 2
while True:
    account_number = input("Enter your 10-digit account number: ")

    if account_number.isdigit() and len(account_number) == 10:
        break
    else:
        print("Invalid account number. Please enter a 10-digit number.")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
