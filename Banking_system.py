class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, owner)
            print(f"Account created for {owner} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


def main():
    banking_system = BankingSystem()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            owner = input("Enter owner name: ")
            banking_system.create_account(account_number, owner)

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = banking_system.get_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = banking_system.get_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = banking_system.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the banking system.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
