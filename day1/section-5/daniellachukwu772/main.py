
'''for :
'''
        for account  in accounts:
    if  account == account_to_search:
         print ("200,account number found")
         break

else:
    print("404,account not found.")
    

'''
 while True:
    account_number = input("Enter your 10-digit account number: ")
  '''  
 if account_number.isdigit() and len(account_number) == 10:
        print("Account number accepted:", account_number)
        break
    else:
        print("Invalid input! Please enter exactly 10 digits.")
