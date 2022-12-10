
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
     
    def deposit(self, amount):
        self.balance += amount
        print("------------")
        print(f"You've deposited ${amount}")
        print(f"Your current balance is ${self.balance}")
        print("------------")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("=================")
            print("Insufficient Funds: Charging a $5 fee")
            print(f'Your current balance now is: ${self.balance}')
            print("=================")
            return self
        else:
            print("------------")
            self.balance -= amount
            print(f"You've withdraw ${amount}")
            print(f"and your current balance is: ${self.balance}")
            print("------------")
            return self

    def display_account_info(self):
        print(f'Your current balance is: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            self.int_rate_conv = int(self.int_rate * 100)
            print(f"Current Balance with {self.int_rate_conv}% interest rate: ${self.balance}")
            return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    # other methods

    def make_deposit(self, amount):
        print(self.account.deposit(amount))
        return self

    def make_withdraw(self, amount):
        print(self.account.deposit(amount))
        return self

    def display_user_balance(self):
        print(f"Account Owner: {self.name}")
        self.account.display_account_info()
        return self



user1 = User("Jake", "jake@j.com")
user1.make_deposit(100).make_deposit(1500).make_deposit(25).make_deposit(25.25).make_withdraw(250).display_user_balance()

# user2 = BankAccount(0.05, 500)
# user2.deposit(1050).deposit(25.99).withdraw(350).withdraw(369.24).withdraw(150.25).withdraw(14).yield_interest().display_account_info()


