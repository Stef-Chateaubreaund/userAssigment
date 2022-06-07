class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}  Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


stef = User("Miss Stef")
Chris = User("Chris")
Leticia = User("Miss Leticia")

stef.make_deposit(500)
stef.make_deposit(100)
stef.make_deposit(350)
stef.make_withdrawl(300)
stef.display_user_balance()

Chris.make_deposit(50)
Chris.make_deposit(50)
Chris.make_withdrawl(50)
Chris.make_withdrawl(30)
Chris.display_user_balance()

Leticia.make_deposit(50)
Leticia.make_withdrawl(30)
Leticia.make_withdrawl(50)
Leticia.make_withdrawl(30)
Leticia.display_user_balance()
