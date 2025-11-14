__author__ = "Ridham Sood"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot, Signal

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from datetime import datetime

class ClientLookupWindow(LookupWindow):
    """A class to display the account details according to the client
    number typed.
    """

    def __init__(self):
        """Initializes the init method.
        """
        super().__init__()

        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.__on_lookup_button)
        self.client_number_edit.textChanged.connect(self.__on_text_change)
        self.account_table.cellClicked.connect(self.__on_select_account)

    @Slot()
    def __on_lookup_button(self):
        """This is a slot method used to get the client number and show
        their account details.
        """
        
        try:
            client_number_entered = int(self.client_number_edit.text())
            self.reset_display()
        except ValueError as e:
            self.reset_display()
            QMessageBox.warning(self, "Input Error", "The client number must be of numeric value.")
            return
        
        if client_number_entered in self.client_listing:
            client = self.client_listing[client_number_entered]
            client_first_name = client.first_name
            client_last_name = client.last_name
            self.client_info_label.setText(f"Client Name: {client_first_name} {client_last_name}")
        else:
            QMessageBox.warning(self, "Not Found", f"Client number: {client_number_entered} not found.")
            return

        self.account_table.setRowCount(0)
        for account in self.accounts.values():
            bank_client_number = account.client_number

            if bank_client_number == client_number_entered:
                
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)

                account_number = QTableWidgetItem(str(account.account_number))
                balance = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created = QTableWidgetItem(str(account._date_created))
                account_type = QTableWidgetItem(type(account).__name__)
                
                self.account_table.setItem(row, 0, account_number)
                self.account_table.setItem(row, 1, balance)
                self.account_table.setItem(row, 2, date_created)
                self.account_table.setItem(row, 3, account_type)

        self.account_table.resizeColumnsToContents()

    @Slot()
    def __on_text_change(self):
        """This is a slot method used to clear the bank account details
        when the user will write the new client number.
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """This is the slot method used to get the cell clicked by the
        user and display the account detail window for that particular
        cell.

        Args:
        row(int): Represents the row of the table.
        column(int): Represents the column of the table.
        """

        selected_account = self.account_table.item(row, 0)
        if selected_account == "":
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid record.")
            return

        selected_number = int(selected_account.text())
        if selected_number in self.accounts:
            bank_account = self.accounts[selected_number]

            accounts_detail = AccountDetailsWindow(bank_account)
            accounts_detail.balance_updated.connect(self.__update_data)
            accounts_detail.exec_()
        else:
            QMessageBox.warning(self, "No Bank Account", "Bank Account selected does not exist.")
            return
        
    @Slot()
    def __update_data(self, account: BankAccount):
        """This is the slot which will receive the signal from the account
        detail window to update the balance of that account number.

        Args:
        account(BankAccount): Represents the bank account type.
        """

        for accounts in range(self.account_table.rowCount()):
            if account.account_number == int(self.account_table.item(accounts, 0).text()):
                self.account_table.item(accounts, 1).setText(f"${account.balance:,.2f}")
                self.accounts[account.account_number] = account
                update_data(account)
                break
