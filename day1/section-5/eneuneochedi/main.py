account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element

response = ""
for acctNum in accounts:
    if acctNum == account_to_search:
        response = "200 - Account found"
    else:
        response = "404 - Account not found"

print(response)
