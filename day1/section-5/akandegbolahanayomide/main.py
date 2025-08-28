# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element


isFound = False

# Use a for loop to check if the account exists
for acc in accounts:
    if acc == account_to_search:
        print("200 - Account found")
        isFound = True
        break  
##
if not isFound:
    print("404 - Account not found")


================================================================================================


while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    # Validates 10-digit numeric account numbers

    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break
    else:
        print("Account number is invalid. Please try again.")
