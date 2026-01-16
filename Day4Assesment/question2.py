class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created:", self.account_number)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")

    def __del__(self):
        print("Account deleted:", self.account_number)

account = BankAccount("ACC123", 5000)

account.deposit(2000)
account.withdraw(3000)
account.withdraw(6000)  # Invalid withdrawal

del account


