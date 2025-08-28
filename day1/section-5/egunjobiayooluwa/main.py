#EXCERCISE ONE******************************************************************************************
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

for account in accounts:
    if account == account_to_search:
        print("202, account found")
        break
else:
    print("404, account not found")

#EXERCISE TWO*******************************************************************************************
while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    while account_number.isdigit() == False or len(account_number) != 10:
        print("Invalid account number. Please try again.")
        account_number = input("Enter your 10-digit account number: ")

    print("Account number accepted.")
    break

