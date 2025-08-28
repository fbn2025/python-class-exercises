while True:
    account_number = input("Enter your 10-digit account number: ")

    if account_number.isdigit() and len(account_number) == 10:
        print(f"Account number {account_number} is valid.")
        break
    else:
        print("Invalid account number. Please try again.")
