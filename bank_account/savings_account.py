"""This module calculates the transactions for the saving account."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """This is the class for the saving account."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """Initializes the init method.
        
        Args:
        account_number(int): Represents the account number of the account
                            holder.
        client_number(int): Represents the client number of the account
                            holder.
        balance(float): Represents the balance of the account holder.
        date_created(date): Represents the date of the transaction.
        minimum_balance(float): Represents the minimum balance of the account.
        
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except:
            self.__minimum_balance = 50
        
        # Declaring private attribute
        self.__strategy = MinimumBalanceStrategy(minimum_balance)

    def __str__(self) -> str:
        """This method returns the formatted message.
        
        Returns:
        str: Returns the formatted string message to the person.
        
        """

        return (
            super().__str__() + f"\nMinimum Balance: ${self.__minimum_balance:.2f}"
            + f"\nAccount Type: Savings"
        )

    def get_service_charge(self) -> float:
        """This method calculates the service charge for the transaction.
        
        Returns:
        float: Returns the service charge charged by the bank.
        
        """

        # Returning service charges with strategy pattern
        return self.__strategy.calculate_service_charges(self)