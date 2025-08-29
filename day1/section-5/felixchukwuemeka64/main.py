while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break
    else:
        print("Invalid account number. Please try again.")
