# List of account numbers
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

# Ask the user to enter an account number
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

#for the while loop
while True:
    account_number = input("Enter your 10-digit account number: ")

    # Keep asking until a valid 10-digit numeric account number is entered

    # Check if it is numeric and exactly 10 digits
    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break  # exit the loop once valid
    else:
        print("❌ Invalid account number. Please try again.")
