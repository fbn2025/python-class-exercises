from abc import ABC, abstractmethod

# Abstract Base Class
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


# Concrete Class
class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def __str__(self):
        return f"Account Holder: {self.name}, Balance: ${self.balance}"


# Subclass
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Interest added at {rate}%. New balance: ${self.balance:.2f}")
        else:
            print("Interest rate must be positive.")



if __name__ == "__main__":
    acc1 = BankAccount("Alice", 1000)
    print(acc1)
    acc1.deposit(50)
    acc1.withdraw(30)
    print(acc1)

    print("\n--- Savings Account Example ---")
    sav_acc = SavingsAccount("Bob", 200)
    print(sav_acc)
    sav_acc.add_interest(5)  # 5% interest
    print(sav_acc)
