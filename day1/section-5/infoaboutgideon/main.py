# Exercise 1 - For Loop

## Exercise 1 – Find an Account (for Loop)

# You are given a list of account numbers:

# ```py
# accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]
# ```

# Task:
# 1. Ask the user to enter an account number.
# 2. Use a for loop to check if the account number exists in the list.
# 3. If it exists, print "200 - Account found".
# 4. Otherwise, print "404 - Account not found"

# ```py
# accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

# user_input = int(input("Please enter account number to check: "))

# for account_number in accounts:
#     if user_input == account_number:
#         print("200 - Account found")
#     else:
#         print("404 - Account not found")
# ```

accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element
account_is_found = False

for account in accounts:
    if account_to_search == account:
        account_is_found = True
        break

print("200 - Account found") if account_is_found else print("404 - Account not found")



## Exercise 2 – Valid Account Number Input (While Loop)

# Banks only accept 10-digit numeric account numbers.

# Task:
# 1. Ask the user to enter their account number.
# 2. Keep asking until they provide a valid 10-digit number (all numbers, length 10).
# 3. Once valid, print "Account number accepted".

# Goal:
# To practice using for loops to search lists, and while loops for input validation.

# Exercise 2 - While Loop
while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
    if len(account_number) == 10 and account_number.isdigit():
        print("Account number accepted")
        break
