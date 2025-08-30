class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
       if amount > 0:
            self.balance += amount # implement this

    def withdraw(self, amount):
       if 0 <= amount <= self.balance:
            self.balance -= amount
       else:
            print("Insufficient funds") # implement this

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            self.balance += self.balance * rate
# Example usage
account = BankAccount("Alice", 1000)
print(account)

savings = SavingsAccount("Bob", 500)
savings.add_interest(0.05)  # 5% interest
print(savings)
