class InsufficientAmount(Exception):
    pass

class Wallet(object):

    def __init__(self, balance):
        self.balance = balance
