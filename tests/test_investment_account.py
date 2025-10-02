"""This module contains the testing of functionality of the investment class."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

import unittest
from bank_account.investing_account import InvestingAccount
from datetime import date

class TestClass(unittest.TestCase):
    """This class contains the tests for investment class."""

    def test_init_set_attributes_to_input_values(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2025, 5, 1), 3.00)

        # Assert
        self.assertEqual(12345, investment._BankAccount__account_number)
        self.assertEqual(123, investment._BankAccount__client_number)
        self.assertEqual(1000, investment._BankAccount__balance)
        self.assertEqual(date(2025, 5, 1), investment._date_created)
        self.assertEqual(3.00, investment._InvestingAccount__management_fee)

    def test_init_invalid_management_fee(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2025, 5, 1), "five")

        # Act
        expected = 2.55

        # Assert
        self.assertEqual(expected, investment._InvestingAccount__management_fee)

    def test_get_service_charge_when_date_more_than_ten_years_ago(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2013, 5, 1), 3.00)

        # Act
        actual = investment.get_service_charge()

        # Assert
        expected = 0.50
        self.assertEqual(actual, expected)

    def test_get_service_charge_when_date_exactly_ten_years_ago(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2015, 10, 2), 3.00)

        # Act
        actual = investment.get_service_charge()

        # Assert
        expected = 0.50
        self.assertEqual(actual, expected)

    def test_get_service_charge_when_date_within_ten_years(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2018, 5, 1), 3.00)

        # Act
        actual = investment.get_service_charge()

        # Assert
        expected = 3.50
        self.assertEqual(actual, expected)

    def test_str_date_more_than_ten_years_ago_display_waived_management_fee(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2013, 5, 1), 3.00)

        # Assert
        expected = (
            f"Account number: 12345\n"
            + f"Balance: $1,000.00\n"
            + f"Date Created: 2013-05-01\n"
            + f"Management Fee: Waived\n"
            + f"Account Type: Investing"
        )

        self.assertEqual(expected, str(investment))

    def test_str_date_within_ten_years_display_management_fee(self):

        # Arrange
        investment = InvestingAccount(12345, 123, 1000, date(2018, 5, 1), 3.00)

        # Assert
        expected = (
            f"Account number: 12345\n"
            + f"Balance: $1,000.00\n"
            + f"Date Created: 2018-05-01\n"
            + f"Management Fee: $3.00\n"
            + f"Account Type: Investing"
        )

        self.assertEqual(expected, str(investment))