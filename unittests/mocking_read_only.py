import unittest
from unittest.mock import Mock, PropertyMock, patch

class BankAccount:
    def __init__(self):
        self._balance = 1000
    
    @property
    def balance(self):
        """Read-only property"""
        return self._balance

class TestBankAccount(unittest.TestCase):
    def test_balance(self):
        with patch.object(BankAccount, 'balance', new_callable=PropertyMock) as mock_balance:
            mock_balance.return_value = 5000
            my_bank = BankAccount()
            self.assertEqual(my_bank.balance, 5000)

if __name__ == "__main__":
    unittest.main()