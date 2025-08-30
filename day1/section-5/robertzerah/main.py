# Exercise 1 - For Loop

accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

def find_account_number(account_to_search, accounts_list):
    if account_to_search in accounts_list:
        return "200, account found"

    return "404, account not found"

account_to_search = input("Enter account number to search: ")
result = find_account_number(account_to_search, accounts)
print(result) 



while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

    if len(account_number) == 10 and account_number.isdigit():
        print("Account number is valid.")
        break
    print("Invalid account number. Please try again.")
