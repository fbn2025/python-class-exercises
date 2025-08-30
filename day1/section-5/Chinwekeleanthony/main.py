# excercise 1
while True:
    account_number = input("Enter your 10-digit account number: ")


    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break  
    else:
        print("Invalid account number. Please try again. ")





# excercise 2
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

found = False
for account in accounts:
    if account == account_to_search:
        found = True
        break

if found:
    print("200-Account found!")
else:
    print("404-Account not found!")
