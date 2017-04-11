# test_wallet_parametrized.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def my_wallet():
	'''Returns an instance of Wallet with balance of 0'''
	return Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
	(30,10,20),
	(20,2,18),
	])

def test_transactions(my_wallet,earned, spent, expected):
	my_wallet.add_cash(earned)
	my_wallet.spend_cash(spent)
	assert my_wallet.balance == expected