"""This file contains the frequent transaction of withdrawals and deposits."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """This class contains the transactions of withdrawals and deposits.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """Initializes the init method to calculate transactions.
        
        Args:
        account_number(int): Represents the account number of the account
                            holder.
        client_number(int): Represents the client number of the account
                            holder.
        balance(float): Represents the balance of the account holder.
        date_created(date): Represents the date of the transaction.
        overdraft_limit(float): Represents the limit of the overdraft.
        overdraft_rate(float): Represents the rate of the overdraft.
        
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = round(0.05, 2)

    def __str__(self) -> str:
        """This method returns the formatted message.
        
        Returns:
        str: The formatted message for the account.
        
        """
        return (
            super().__str__() + f"\nOverdraft Limit: ${self.__overdraft_limit:,.2f}"
            + f"\nOverdraft rate: ${self.__overdraft_rate * 100:,.2f}%\nAccount Type: "
            + f"Chequing"
        )
    
    def get_service_charge(self) -> float:
        """Calculates the service charge of the bank.
        
        Returns:
        float: The calculated service charge for the transaction.
        
        """
        balance = self._BankAccount__balance

        if balance >= self.__overdraft_limit:
            charge = self.BASE_SERVICE_CHARGE
        else:
            charge = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - balance)\
                * self.__overdraft_rate
            
        return charge
