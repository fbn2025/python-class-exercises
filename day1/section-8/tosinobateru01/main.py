
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        new_balance = self.balance + amount
        return f"Your new acount balance is {new_balance}. A total of {amount} was deposited."


    def withdraw(self, amount):
        left_balance = self.balance - amount
        if left_balance < 0:
            return f"Oops!!! You don't have enough money in your account. Your balance is {self.balance}"
        else:
            return f"{amount} successfuly withdrawed! Your balance is {left_balance}."
       

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def add_interest(self,rate):
        interest = self.balance + (self.balance * (rate/100))
        return f"Your new balance with rate interest is {interest:.2f}"    

account = BankAccount("Tosin Obateru", 1000000)
deposit = account.deposit(100000)
withdraw = account.withdraw(100000)
print(account)
print(deposit)
print(withdraw)


