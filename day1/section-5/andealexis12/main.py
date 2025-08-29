# FOR LOOP EXERCISE
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]
accounts_to_search = input("Enter the account you are looking for: ")

for account_number in accounts:
    if accounts_to_search == account_number:
        print("200, account found")
        break
else:
    print("400, account not found")


# WHILE LOOP EXERCISE

while True:
    account_to_search = input("Enter your 10-digit account number: ")

    if account_to_search.isdigit() and len(account_to_search) == 10:
        print("Account number accepted")
        break
    else:
        print("Invalid input. Please enter a 10-digit numeric account number.")

