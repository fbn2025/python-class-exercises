# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element
# account_is_found = False
for account_number in accounts:
    if account_to_search == account_number:
        print("account_is_found")
    else:
        print("Not_Found")
    break
