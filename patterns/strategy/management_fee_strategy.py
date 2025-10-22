"""This file contains the strategy pattern for management fee situation."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """This class contains the strategy pattern for management fee."""

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """Initializes an init method.
        
        Args:
        date_created(date): Represents the date of the transactions.
        management_fee(float): Represents the management fee to be charged.
        """

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """This method calculates the service charges to be applied.
        
        Args:
        account(BankAccount): Represents the Bank account to which the
                            charges will apply.
        
        Return:
        float: The service charge to be applied.
        """
        date = self.TEN_YEARS_AGO

        if self.__date_created < date:
            charge = self.BASE_SERVICE_CHARGE
        else:
            charge = self.BASE_SERVICE_CHARGE + self.__management_fee
        
        return charge