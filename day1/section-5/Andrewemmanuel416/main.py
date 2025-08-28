# List of account numbers
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

# Asks the user to enter an account number
account_to_search= input("Enter account to search: ")

# Flag to track if found
found = False

# Use a for loop to check if the account exists
for acc in accounts:
    if acc == account_to_search:
        print("200 - Account found")
        found = True
        break  # stop searching once found

# If not found after loop
if not found:
    print("404 - Account not found")
