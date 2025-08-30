# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element
account_is_found = False

for account_number in accounts:
     if account_number == account_to_search:
        account_is_found = True

if account_is_found == True:
            print("200 - account_is_found")
         
else:
            print("400 - account_is_not_found")



# Exercise 2 - While Loop
while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted.")
        break

