# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

for account_number in accounts: 
 if account_to_search == account_number:
    print ("200 - Account Found")
    break
 else:
  print("404 - Account not found")
  break

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

# while Loop
while True:
    account_number = input("Enter your 10-digit account number: ")

    while account_number.isdigit() == False or len(account_number) != 10:
        print("Invalid Account Number")
        account_number = input ("Enter your 10-digit account number: ")

    print("Account number accepted")   
    break
    

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
