while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
    if len(account_number) == 10 and account_number.isdigit():
        break
    else:
        continue
