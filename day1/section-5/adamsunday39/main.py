# Exercise 2 – Valid Account Number Input (While Loop)

# Banks only accept 10-digit numeric account numbers
while True:
    account_number = input("Enter your 10-digit account number: ")

    # Keep it as a string so leading zeros are preserved
    if account_number.isdigit() and len(account_number) == 10:
        print(f"Account number accepted: {account_number}")
        break
    else:
        print("Invalid account number. Please try again.")
