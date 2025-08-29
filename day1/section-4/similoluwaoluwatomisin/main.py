# Exercise 1 - For Loop
# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

found = False
for account in accounts:
    if account == account_to_search:
        found = True
        break
if found:
    print("200 Account found.")
else:
    print("404 Account not found.")  

