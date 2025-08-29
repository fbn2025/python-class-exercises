not_correct = True 
while not_correct:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    if len(account_number) == 10: 
        print("Account number accepted")
        not_correct = False 
    else: 
        account_number = input("Enter your 10-digit account number: ") 
