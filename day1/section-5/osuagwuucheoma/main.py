# Exercise 1 - For Loop
accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

# Loop through the accounts list
found = False  # This will track if the account was found

for account in accounts:
    if account_to_search == account:
        print("200 - Account found")
        found = True
        break  # Stop the loop because we found the account

else:
    print("404 - Account not found")


# The solution/code below is for the second task i.e "The While Loop"
while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

   # 1. Is account upto 10 digits, if not keep iterating
  #  2. Go through each of the digits to ensure they are all numbers and not letters/alphabets/characters

    if account_number.isdigit() == True and len(account_number) == 10:
        print("Valid")
        break
    else:
        continue
