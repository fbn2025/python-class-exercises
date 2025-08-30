## Exercise 1 – Find an Account (for Loop)

accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

found = False
for account in accounts:
    if account == account_to_search:
        found = True
        break

if found:
    print("200- Account found!")
else:
    print("404- Account not found!")
    
/
# Exercise: Continuously prompt the user to enter a valid 10-digit account number.

while True:
    account_number = input("Enter your 10-digit account number: ")
    
    # Check if the account number has only digits and length is 10
    if account_number.isdigit() and len(account_number) == 10:
        print ("Thank you! Your account number is valid and accepted.")
        break
    else:
        print("Invalid input! Please Kindly enter your exact 10 digits.")
