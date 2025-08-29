# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

for account in accounts:
    if account == account_to_search:
        print("Account found!")
        break
else:
        print("Account not found.")

#the second assignment class exercise is below

account_number = input("Enter your 10-digit account number: ")
while account_number:
    if len(account_number) == 10 and account_number.isdigit():
        print("Account number accepted.")
        break
    else:
        print("Invalid account number. Please try again.")
        break
