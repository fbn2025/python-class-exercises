# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")
for account_number in accounts:
    if account_to_search == account_number:
        print("Account found!")
        break 
else:
    print("Account not found.")

# Exercise 2 - While Loop

while True:
    account_number = input("Enter your 10-digit account number: ")

    if account_number.isdigit() and len(account_number) == 10:
        print("Valid account number entered:", account_number)
        break
    else:
        print("Invalid account number. Please try again.")
