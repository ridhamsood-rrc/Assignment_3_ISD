"""This file contains the strategy pattern applied to the BankAccount."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """This class contains the pattern to apply on service charge."""

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """This method calculates the service charges.
        
        Args:
        account(BankAccount): Represents the Bank account to which the
                            charges will apply.
        
        Return:
        float: The service charge to be applied.
        """
        pass