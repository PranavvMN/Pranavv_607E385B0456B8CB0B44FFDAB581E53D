class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name} ({self.__account_number}): ${self.__account_balance}")

# Creating an instance of BankAccount
account = BankAccount("260325005", "pranavv", 1000.0)

# Testing deposit and withdraw functionality
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
