from abc import ABC, abstractmethod

class AbstractBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def __str__(self):
        pass

class BankAccount(AbstractBankAccount):
    def __init__(self, customer_name, balance=0):
         self.customer_name = customer_name
         self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero (0)")
        else:
            self.balance += amount
            print(f"Amount deposited: {amount}. New balance: {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero (0)")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}. New balance: {self.balance}.")

    def __str__(self):
        return (f"Account holder: {self.customer_name}. \tBalance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, balance=0):
        super().__init__(customer_name, balance)

    def add_interest(self, interest_rate):
        if interest_rate < 0:
            print("Interest rate must be positive")
        else:
            earned_interest = self.balance * (interest_rate / 100)
            self.balance += earned_interest
            print(f"Accrued interest: {earned_interest} @{interest_rate}% pa. New balance: {self.balance}")


savings = SavingsAccount("Ayoose", 2000)
print(f"\tWelcome to ABC Bank \n{savings}")
savings.deposit(1500)
savings.withdraw(500)
savings.add_interest(10)

print(savings)
