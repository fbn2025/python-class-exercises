## Exercise 1 – Find an Account (for Loop) - 5.4

accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Please enter your account number for search: ")

for account_number in accounts:
    if account_to_search == account_number:
        print("200, account found")
        break 
else:
    print("404, account not found")



# Exercise 2 – Valid Account Number Input (While Loop + For Loop)

while True:
    account_number = input("Enter your account number: ")

    if len(account_number) == 10:
        all_digits = True  

        for char in account_number:
            if not char.isdigit():
                all_digits = False
                break 

        if all_digits:
            print("Account number accepted")
            break
        else:
            print("Invalid account number. Only digits allowed.")
    else:
        print("Invalid account number. Must be exactly 10 digits.")


