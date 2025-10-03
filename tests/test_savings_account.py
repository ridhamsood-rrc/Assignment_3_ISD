"""This module contains the test to validate the functionality of saving class.
"""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestClass(unittest.TestCase):
    """This class defines the tests."""

    def test_init_set_attributes_to_input_values(self):

        # Arrange
        saving = SavingsAccount(12345, 123, 1000, date(2025, 5, 1), 30.0)

        # Assert
        self.assertEqual(12345, saving._BankAccount__account_number)
        self.assertEqual(123, saving._BankAccount__client_number)
        self.assertEqual(1000, saving._BankAccount__balance)
        self.assertEqual(date(2025, 5, 1), saving._date_created)
        self.assertEqual(30.0, saving._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance(self):

        # Arrange
        saving = SavingsAccount(12345, 123, 1000, date(2025, 5, 1), "thirty")

        # Act
        expected = 50

        # Assert
        self.assertEqual(expected, saving._SavingsAccount__minimum_balance)

    def test_get_service_charge_balance_greater_than_minimum_balance(self):

        # Arrange
        saving = SavingsAccount(12345, 123, 1000, date(2025, 5, 1), 40)

        # Act
        actual = saving.get_service_charge()

        # Assert
        expected = 0.50
        self.assertEqual(actual, expected)

    def test_get_service_charge_balance_equal_to_minimum_balance(self):

        # Arrange
        saving = SavingsAccount(12345, 123, 200, date(2025, 5, 1), 200)

        # Act
        actual = saving.get_service_charge()

        # Assert
        expected = 0.50
        self.assertEqual(actual, expected)

    def test_get_service_charge_balance_less_than_minimum_balance(self):

        # Arrange
        saving = SavingsAccount(12345, 123, 50, date(2025, 5, 1), 100)

        # Act
        actual = saving.get_service_charge()

        # Assert
        expected = 1
        self.assertEqual(actual, expected)

    def test_str_returns_correct_message(self):

        # Arrange
        saving = SavingsAccount(12345, 123, 1000, date(2025, 5, 1), 40)

        # Assert
        expected = (
            f"Account number: 12345\n"
            + f"Balance: $1,000.00\n"
            + f"Minimum Balance: $40.00\n"
            + f"Account Type: Savings"
        )
        self.assertEqual(expected, str(saving))