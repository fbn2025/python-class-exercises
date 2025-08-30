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

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
         self.name = name
         self.balance = balance
         self.total_deposited = 0
         self.total_withdrawn = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.total_deposited += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        self.total_withdrawn += amount

    def __str__(self):
        return (f"{self.name} has a balance of {self.balance} after he deposited: {self.total_deposited}, and withdrew: {self.total_withdrawn}.")

# TODO: Create a SavingsAccount class that inherits from BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        self.interest_earned = 0

    def interest_gained(self):
        if self.interest_rate < 0:
            raise ValueError("Interest rate must be positive")
        self.interest_earned = self.balance * (self.interest_rate/100)
        return self.interest_earned

    def apply_interest(self):
        interest = self.interest_gained()
        self.balance += interest
        return self.balance
    def __str__(self):
        return (f"{self.name} has a current balance of {self.balance} because he deposited {self.total_deposited}, withdrew {self.total_withdrawn}\n"
                f"and his savings account has an interest rate of {self.interest_rate}% which earned him an additional {self.interest_earned}.")




saver = SavingsAccount("Emmanuel", 2000, 10)
saver.deposit(1500)
saver.withdraw(500)
saver.apply_interest()

print(saver)
