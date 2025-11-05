"""
Bank Account Management System
This class represents a bank account with the following features:
- Attributes: account number, account holder name, balance
- Methods:
  * deposit(): Adds money to account with validation
  * withdrawl(): Removes money from account with balance check
  * bankFees(): Calculates 5% service charge on current balance
  * display(): Shows complete account information
"""

class bankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdrawl(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount")

    def bankFees(self):
        fees = self.balance * 0.05
        return fees

    def display(self):
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)
        print("Bank Fees (5%):", self.bankFees())
        print()

account = bankAccount(12345, "adarsh", 1000)
account.display()
account.deposit(1000)
account.display()
account.withdrawl(500)
account.display()
