#Q4. BankAccount with history. Write a BankAccount class with owner, a balance and a list history. Add deposit(amount) and withdraw(amount). Each action adds a line to history like "deposit 500". If someone withdraws more than the balance or deposits a negative amount, raise ValueError("..."). Then call the methods inside try/except so the program never crashes, and print the history at the end.
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.history.append(f"deposit {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.history.append(f"withdraw {amount}")

account = BankAccount("Alice")
try:
    account.deposit(500)
    account.withdraw(200)
    account.deposit(-100)  
except ValueError as e:
    print(f"Error: {e}")

print("Transaction History:")
for transaction in account.history:
    print(transaction)