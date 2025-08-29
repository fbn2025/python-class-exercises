# ASSIGNMENT 5.4, FOR LOOP

accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

# Ask the user to enter an account number
user_input = input("Enter your account number: ")

# Flag to track if account is found
found = False

# Loop through the list to check for a match
for account in accounts:
    if user_input == account:
        print("200 - Account found")
        found = True
        break
# If not found after the loop
if not found:
    print("404 - Account not found")



# for assignment 5.5, while loop
while True:
    account_number = input("Enter your 10-digit account number: ")

    # Check if it's all digits and exactly 10 characters long
    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break
    else:
        print("Invalid account number. Please enter exactly 10 digits.")
