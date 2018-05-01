class InsufficientAmount(Exception):
    pass

class Wallet(object):

    def __init__(self, balance=0):
        self.balance = balance
