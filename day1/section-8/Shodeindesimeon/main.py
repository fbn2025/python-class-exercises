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
    """
    A basic bank account with deposit, withdrawal, and balance tracking.
    """
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
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.total_withdrawn += amount

    def __str__(self):
        return f"{self.name} has a balance of {self.balance:.2f} " \
               f"(Deposited: {self.total_deposited:.2f}, " \
               f"Withdrew: {self.total_withdrawn:.2f})"


class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.0):
        super().__init__(name, balance)
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        self.interest_rate = interest_rate
        self.interest_earned = 0  # Accumulated interest over time

    def apply_interest(self):
        """Apply interest based on current balance and interest rate."""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        self.interest_earned += interest
        return interest  # Returns how much was added

    def __str__(self):
        return f"{self.name} has a current balance of {self.balance:.2f} " \
               f"(Deposited: {self.total_deposited:.2f}, " \
               f"Withdrew: {self.total_withdrawn:.2f})\n" \
               f"Savings interest rate: {self.interest_rate}%, " \
               f"Total interest earned: {self.interest_earned:.2f}"


# --- Example usage ---
if __name__ == "__main__":
    # Example for a Regular bank account
    account = BankAccount("Alice", 1000)
    account.deposit(500)
    account.withdraw(300)
    print(account)
    print()

    # Example for a Savings account
    savings = SavingsAccount("Osinachi", 5000, interest_rate=5)
    savings.deposit(1000)
    savings.withdraw(600)
    interest_added = savings.apply_interest()
    print(f"Interest applied: {interest_added:.2f}")
    print(savings)
