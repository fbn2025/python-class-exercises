accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Please enter your account number for search: ")

for account_number in accounts:
    if account_to_search == account_number:
        print("200, account found")
        break 
else:
    print("account not found")




# 5.1

