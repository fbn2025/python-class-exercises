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
