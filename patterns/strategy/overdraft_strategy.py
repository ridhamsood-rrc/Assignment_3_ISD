"""This file contains the design pattern for overdraft situation."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """This class creates the design pattern for overdraft."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """Initializes the init method.
        
        Args:
        overdraft_limit(float): Represents the overdraft limit of the
                                account.
        
        overdraft_rate(float): Represents the overdraft rate applied.
        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """This method calculates the service charges to be applied.
        
        Args:
        account(BankAccount): Represents the Bank account to which the
                            charges will apply.
        
        Return:
        float: The service charge to be applied.
        """
        balance = account.balance

        if balance >= self.__overdraft_limit:
            charge = self.BASE_SERVICE_CHARGE
        else:
            charge = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - balance)\
                * self.__overdraft_rate
            
        return charge