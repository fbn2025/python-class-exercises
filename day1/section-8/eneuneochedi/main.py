## Class Exercise on OOP
from abc import ABC, abstractmethod
from datetime import datetime

#Abstract class
class AbstractBankAccount(ABC):

    @abstractmethod
    def deposit(self, deposit_amount):
        pass

    @abstractmethod
    def withdraw(self, withdrawal_amount):
        pass

    @abstractmethod
    def __str__(self):
        pass


class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.transactionDescription = ""
        self.txn_alert = False
        self.currency = "NGN "
        self.new_account_opening = True

        if balance >= 0:
            self.balance = balance
            
        else:
            print(f"Initial account can't be in deficit {self.currency}{balance}: account has been created with zero balance.")
            #self.balance = 0


    def deposit(self, deposit_amount):
        
        if deposit_amount > 0:
            self.deposit = deposit_amount
            self.balance += self.deposit
            #self.transactionDescription = f" after a deposit of {self.deposit}"
            self.transactionDescription = "Cash Deposit"

            #Extra
            self.txn_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.txn_type = "Credit"
            self.txn_alert = True
            self.new_account_opening = False
            self.txn_amount = self.deposit
        else:
            print(f"\nInvalid deposit amount {deposit_amount}")
            self.new_account_opening = False
        

    def withdraw(self, withdrawal_amount):
        self.new_account_opening = False
        self.txn_alert = False

        if withdrawal_amount >= 0 and self.balance > withdrawal_amount:
            self.withdrawal = withdrawal_amount
            self.balance -= self.withdrawal
            self.transactionDescription = "ATM Withdrawal"
            #self.transactionDescription = f" after a withdrawal of {self.withdrawal}"

            #Extra
            self.txn_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.txn_type = "Debit"
            self.txn_alert = True
            self.txn_amount = self.withdrawal

        elif withdrawal_amount > self.balance:
            print(f"Insufficient funds. Withdrawal of {withdrawal_amount} is above your balance of {self.balance}.", end=" ")
            print("You're not qualified for overdraft")

        else:
            print(f"\nInvalid withdrawal amount! {withdrawal_amount}")

        #return self.withdrawal"

    def __str__(self):
        if self.txn_alert: 
            line_sep = "\n___________________________________\n***********************************\n"
            return f"{line_sep}Txn: {self.txn_type}\nAcct.: {self.name}\nAmount: {self.currency}{self.txn_amount}\nDesc.: {self.transactionDescription}\nDate: {self.txn_time}\nBal.: {self.currency}{self.balance}\nThanks for Banking with us.{line_sep}"
        
        elif self.new_account_opening and not(self.txn_alert):
            return f"\nCongratulations! New account has been created for {self.name} with an initial balance of {self.currency}{self.balance}{self.transactionDescription}"
        else:
            return ""
        

# TODO: Create a SavingsAccount class that inherits from BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance=0)
        self.new_account_opening = True
        self.txn_alert = False
        if balance >= 0:
            self.balance = balance  
              
        else:
        
            print(f"Initial account can't be in deficit {balance}: account has been created with zero balance.")
            #self.balance = 0

        

    def savingsDeposit(self, deposit):
        super().deposit(deposit)
    
    def savingsWithdraw(self, withdrawal):
        super().withdraw(withdrawal)
        
    
    def add_interest(self, rate=5):
        if self.balance > 0 and rate > 0:
            self.interest_amount = self.balance * (rate / 100)
            self.balance += self.interest_amount
            
            self.transactionDescription = f"Interest payment, {rate}% p.a"
            self.txn_amount = self.interest_amount
            self.txn_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.txn_type = "Credit"
            self.txn_alert = True
            self.new_account_opening = False
        else:
            print(f"No available balance to calculate rate, deposit some money to start earning interests as high as {rate}% per anum")



# Example usage

account1 = SavingsAccount("Alice", 1000)
print(account1)

account1.savingsDeposit(-25000)
print(account1)

account1.savingsWithdraw(15000)
print(account1)

account1.add_interest(23)
print(account1)
