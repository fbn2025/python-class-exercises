# Exercise 1 - (For Loop)
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

account_found = False

for account in accounts:
    if account == account_to_search:
        account_found = True
        break 

if account_found:
    print("200 - Account found")
else:
    print("404 - Account not found")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

# Exercise 2 - (While Loop)
while True:
    
    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
    account_number = input("Enter your 10-digit account number: ")

    if len(account_number) == 10 and account_number.isdigit():
        print("Account number accepted")
        break

    else:
        print("Invalid input. Must be exactly 10 digit. Try again.")
