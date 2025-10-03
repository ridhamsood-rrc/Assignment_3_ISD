"""This module calculates the transactions for investing account."""

__author__ = "Ridham Sood"
__Version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """This class calculates the transaction of the investing account."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """Initializes the init method.
        
        Args:
        account_number(int): Represents the account number of the person.
        client_number(int): Represents the client number of the person.
        balance(float): Represents the balance of the account.
        date_created(date): Represents the date of the transactions.
        management_fee(float): Represents the fee for the management.
        
        """

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

    def __str__(self) -> str:
        """This method returns the formatted string.
        
        Returns:
        str: Returns the formatted string for the investment account.
        
        """

        date = self.TEN_YEARS_AGO

        if date <= self._date_created:
            message = f"\nDate Created: {self._date_created}\n"\
                    + f"Management Fee: ${self.__management_fee:.2f}\n"\
                    + f"Account Type: Investing"
        else:
            message = f"\nDate Created: {self._date_created}\n"\
                    + f"Management Fee: Waived\n"\
                    + f"Account Type: Investing"
        
        return (
            super().__str__() + message
        )

    def get_service_charge(self) -> float:
        """This method will return the service charge.
        
        Return:
        float: Returns the service charges charged by the bank.
        
        """
        date = self.TEN_YEARS_AGO

        if self._date_created < date:
            charge = self.BASE_SERVICE_CHARGE
        else:
            charge = self.BASE_SERVICE_CHARGE + self.__management_fee
        
        return charge