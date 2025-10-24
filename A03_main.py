"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client


# 2. Create a Client object with data of your choice.
client = Client(123, "Ridham", "Sood", "ridham9@gmail.com")


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing = ChequingAccount(12345, client.client_number, 500, date(2025, 5, 1), 100, 0.02)
saving = SavingsAccount(12345, client.client_number, 500, date(2025, 5, 10), 200)


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing.attach(client)
saving.attach(client)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
other_client = Client(542, "Stephen", "Curry", "stephcurry30@gmail.com")
other_saving = SavingsAccount(12536, other_client.client_number, 800, date(2025, 3, 25), 500)

other_saving.attach(other_client)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

print()
print("--Transactions--")
print()
try:
    chequing.deposit(20000)
    chequing.withdraw(500)
    chequing.withdraw(50000)
except ValueError as e:
    print(e)

try:
    other_saving.deposit(50000)
    other_saving.withdraw(800000)
    other_saving.withdraw(5000)
    
except ValueError as e:
    print(e)