# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# Use a for loop to check if account_to_search is in accounts
found = False
for account in accounts:
    if account_to_search == account:
        found = True
        break   # stop checking once found

if found:
    print("200 - Account found")
else:
    print("404 - Account not found")


# Exercise 2 – Valid Account Number Input (While Loop)

while True:
    account_number = input("Enter your 10-digit account number: ")

    # Check: must be digits only and exactly 10 characters long
    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break   # exit loop when valid
    else:
        print("Invalid account number. Please try again.\n")
