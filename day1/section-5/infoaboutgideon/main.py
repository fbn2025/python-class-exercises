while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
    if len(account_number) == 10:
        for digit in account_number:
            if int(digit):
                continue
        break
    else:
        continue
