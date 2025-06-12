# Build a simple bank account with deposit and withdrawal methods.

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an initial balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        try:
            if amount > 0:
                self.balance += amount
                print(f"Deposited: ${amount:.2f}\n New balance: ${self.balance:.2f}.")
            else:
                print("Deposit amount must be positive.")
        except (ValueError,TypeError):
            print("There is nothigng to deposit. Please enter a valid amount.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
    
    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance
    
def save_balance(balance, filename="balance.txt"):
    with open(filename, "w") as f:
        f.write(str(balance))

def load_balance(filename="balance.txt"):
    try:
        with open(filename, "r") as f:
            return float(f.read())
    except (FileNotFoundError, ValueError):
        return 0.0  # Default balance if file doesn't exist or is invalid
    
if __name__ == "__main__":
    # Load balance from file
    balance = load_balance()
    account = BankAccount(balance)
    while True:
        select = input("1)Deposit\n2)Withdraw\n3)Check Balance\n4)Exit\nSelect an option: ")
        if select == '3':
            print(f"Current balance: ${account.get_balance():.2f}")
        elif select == '4':
            print(f"Final balance: ${account.get_balance():.2f}")
            save_balance(account.get_balance())
            break
        elif select == '1':
            try:
                amount = float(input("Deposit amount: "))
                account.deposit(amount)
                save_balance(account.get_balance())
            except ValueError:
                print("Please enter a valid number.")
        elif select == '2':
            try:
                amount = float(input("Withdraw amount: "))
                account.withdraw(amount)
                save_balance(account.get_balance())
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid selection. Please choose a valid option.")

