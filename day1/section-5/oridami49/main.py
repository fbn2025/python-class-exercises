# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the account_to_search to the looped element
for account_number in accounts:
    if account_to_search == account_number:
        print("200 - Account found!")
        break
    print("404 - Account not found.")
    break



# Exercise 2 – Valid Account Number Input (While Loop)

while True:
    account_number = input("Enter your 10-digit account number: ")

    # Check: must be digits only and exactly 10 characters long
    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break   # exit loop when valid
    else:
        print("Invalid account number. Please try again.\n")
