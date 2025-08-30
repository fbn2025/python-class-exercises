# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element 

# solution
found = False

for account in accounts: 
    if account_to_search == account:
        found = True
        break    # (Stop the loop once we find the account)
    
if found:
    print("Account found!")
else:
    print("Account not found!")



# Exercise 1 - While Loop
while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
#solution

    if account_number.isdigit() and len(account_number) == 10:
        print("Valid account number.")
        break
    else:
        print("Invalid account number, please enter exactly 10 digits")

