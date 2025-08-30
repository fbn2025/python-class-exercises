
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element


for account  in accounts:
    if  account == account_to_search:
         print ("200,account number found")
         break

    else:
        print("404,account not found.")

''' while true'''

while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted:", account_number)
        break
    else:
        print("Invalid input! Please enter exactly 10 digits.")


