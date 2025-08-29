while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    if len(account_number) == 10 and account_number.isdigit():
        print("Account number accepted")
        break   
    else:
        print("Invalid input. Please try again.")



#The for loop exercise:
# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

for acc in accounts:
    if account_to_search == acc:
        print("200 - Account found, please, proceed.")
        break
else:
    print("404 - Account not found, try again!")


