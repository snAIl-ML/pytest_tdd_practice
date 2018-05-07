"Wallet Example"
class InsufficientAmount(Exception):
    "InsufficientAmount Class for edge case"
    pass

class Wallet(object):
    "Wallet Class for balance and several functions"
    def __init__(self, balance=0):
        self.balance = balance

    def add_cash(self, amount):
        "Addition of money"
        self.balance += amount

    def spend_cash(self, amount):
        ""
        if self.balance < amount:
            raise InsufficientAmount('You do not have that much money')
        self.balance -= amount
