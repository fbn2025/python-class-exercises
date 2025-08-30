# Exercise  - FOR Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")


for account in accounts:
    if account_to_search == account:
        print("200 - account found")
        break
    
else:
    print("404 - account not found")







# Exercise - WHILE loop
account = input("Enter account number not letters to search: ")

while account:
    if len(account) == 10 and account.isdigit():
        print("valid account - Account accepted")
        break
 
    else:
        print("Invalid account, enter a ten digits valid account number")
        break
