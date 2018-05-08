# test_wallet.py
'Test for wallet.py'
import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    'Test initialization default'
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    'Test initialization given vale'
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    'Test function add_cash'
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    'Test function spend_cash'
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    'Error raising test'
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
