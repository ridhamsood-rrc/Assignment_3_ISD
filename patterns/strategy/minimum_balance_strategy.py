"""This file contains the design pattern for minimum balance situation."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """This class creates the design pattern for minimum balance situation."""

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """Initializes the init method.
        
        Args:
        minimum_balance(float): Represents the minimum balance of the
                                account.
        """

        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """This method calculates the service charges to be applied.
        
        Args:
        account(BankAccount): Represents the Bank account to which the
                            charges will apply.
        
        Return:
        float: The service charge to be applied.

        """
        if account.balance >= self.__minimum_balance:
            charge = self.BASE_SERVICE_CHARGE
        else:
            charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

        return charge