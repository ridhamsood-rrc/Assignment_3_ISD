"""This module test the functioning of the chequing account."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from bank_account.chequing_account import ChequingAccount
from bank_account.bank_account import BankAccount
import unittest
from datetime import date

class TestClass(unittest.TestCase):
    """Tests the functioning of the chequing account."""

    def setUp(self):

        # Arrange
        self.chequing = ChequingAccount(12345, 123, 1000, date(2025, 5, 1), 400, 0.02)

    def test_init_set_attributes_to_input_values(self):
        # Arrange done above

        # Assert
        self.assertEqual(12345, self.chequing._BankAccount__account_number)
        self.assertEqual(123, self.chequing._BankAccount__client_number)
        self.assertEqual(1000, self.chequing._BankAccount__balance)
        self.assertEqual(date(2025, 5, 1), self.chequing._date_created)
        self.assertEqual(400, self.chequing._ChequingAccount__overdraft_limit)
        self.assertEqual(0.02, self.chequing._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit(self):

        # Arrange
        account = ChequingAccount(12345, 123, 1000, date(2025, 5, 1), "four hundred", 0.02)

        # Act
        expected = -100

        # Assert
        self.assertEqual(expected, account._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate(self):

        # Arrange
        account = ChequingAccount(12345, 123, 1000, date(2025, 5, 1), 400, "two")

        # Act
        expected = 0.05

        # Assert
        self.assertEqual(expected, round(account._ChequingAccount__overdraft_rate, 2))
    
    def test_init_invalid_date(self):

        # Arrange
        account = ChequingAccount(12345, 123, 1000, "2025/5/1", 400, 0.02)

        # Act
        expected = date.today()

        # Assert
        self.assertEqual(expected, account._date_created)

    def test_get_service_charge_greater_balance(self):

        # Arrange
        account = ChequingAccount(12345, 123, 1000, date(2025, 5, 1), 500, 0.02)

        # Act
        actual = account.get_service_charge()

        # Assert
        expected = 0.50
        self.assertEqual(expected, actual)

    def test_get_service_charge_equal_balance(self):

        # Arrange
        account = ChequingAccount(12345, 123, 500, date(2025, 5, 1), 500, 0.02)

        # Act
        actual = account.get_service_charge()

        # Assert
        expected = 0.50
        self.assertEqual(expected, actual)

    def test_get_service_charge_less_balance(self):

        # Arrange
        account = ChequingAccount(12345, 123, 200, date(2025, 5, 1), 500, 0.02)

        # Act
        actual = account.get_service_charge()

        # Assert
        expected = 6.50
        self.assertEqual(expected, actual)

    def test_str_valid_details(self):

        # Arrange & Act
        account = ChequingAccount(12345, 123, 1000, date(2025, 5, 1), 500, 0.02)

        # Assert
        expected = (
                f"Account number: 12345\n"
                + f"Balance: $1,000.00"
                + f"\nOverdraft Limit: $500.00"
                + f"\nOverdraft rate: $2.00%"
                + f"\nAccount Type: Chequing"
                )
        self.assertEqual(expected, str(account))