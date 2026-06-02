class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")



    def get_balance(self):
        return self.balance

if __name__ == "__main__":    
    account = BankAccount("123456789", 2000)
    account.deposit(500)
    # account.withdraw(200)
    print(f"Current balance: ${account.get_balance()}")