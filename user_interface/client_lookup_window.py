__author__ = "ACE Faculty"
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
    """"""

    def __init__(self):
        """Initializes the init method"""
        super().__init__()

        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.on_lookup_button)

    @Slot()
    def on_lookup_button(self):
        """"""
        
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