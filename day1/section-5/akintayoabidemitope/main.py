## Exercise 1 – Find an Account (for Loop)
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

found = False
for account in accounts:
    if account == account_to_search:
        found = True
        break

if found:
    print("Account found!")
else:
    print("Account not found.")
    

# Exercise: Continuously prompt the user to enter a valid 10-digit account number.
# A valid account number should consist only of digits and be exactly 10 characters long.
while True:
    account_number = input("Enter your 10-digit account number: ")
    
    # Check if the account number has only digits and length is 10
    if account_number.isdigit() and len(account_number) == 10:
        break  # valid input, exit the loop
    else:
        print("Invalid input. Please enter exactly 10 digits.")
    # If valid -> break loop, else keep asking
