accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

for acc in accounts:
    if acc == account_to_search :
        print("200 - Account found, please, proceed")
        break
else:
    print("404 - Account not found, please, try again")
