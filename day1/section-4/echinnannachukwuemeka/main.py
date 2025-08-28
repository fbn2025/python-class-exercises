score = int(input("Enter your exam score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
elif score >= 70:
    print("Your grade is A")
elif 60 <= score < 70:
    print("Your grade is B")
elif 50 <= score < 60:
    print("Your grade is C")
elif 40 <= score < 50:
    print("Your grade is D")
elif 0 <= score < 40:
    print("Your grade is F")
else:
    print("Invalid input. Please enter a numeric score.")




accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]
    
account_to_search = input("Enter account number to search: ")
    
for account in accounts:
    if account == account_to_search:
            print("Account found.")
            break
print("Account not found.")
