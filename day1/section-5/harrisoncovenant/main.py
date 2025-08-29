accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")
for account_number in accounts:
    if account_to_search == account_number:
        print("200 - Account found!")
        break
    print("404 - Account not found.")
    break


# Exercise 2 – Valid Account Number Input (While Loop)

while True:
    account_number = input("Enter your 10-digit account number: ")
    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break
    else:
        print("Invalid account number. Please try again.\n")
