#-------------------------------------------
#             EXERCISE 1
#*******************************************
account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

response = ""
for acctNum in accounts:
    if acctNum == account_to_search:
        response = "200 - Account found"
        break
    else:
        response = "404 - Account not found"

print(response)

#-------------------------------------------
#             EXERCISE - 2
#*******************************************
prompt = "Enter your 10-digit account number: "

while True:
    account_number = input(f"{prompt}")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted")
        break
    else:
        prompt = "Invalid account number, enter again: "
