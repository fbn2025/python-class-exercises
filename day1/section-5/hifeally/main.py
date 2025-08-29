# Exercise 1 - For Loop
# accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

# account_to_search = input("Enter account number to search: ")

# # TODO: use a for loop to check if search_account is in accounts
# # Hint: loop through accounts and compare the `account_to_search` to the looped element
# for i in range(4):
#     if accounts[i] == account_to_search:
#         print("200 \nAccount found")
#         break
# else:
#     print("404 \nAccount not found")


# part 2

while True:
    account_number = input("Enter your 10-digit account number: ")

    if account_number.isdigit() and len(account_number) == 10:
        print("Valid account number entered: ", account_number)
        break
    else:
        print("Invalid input. Please enter a valid 10-digit account number and try again.")

    
