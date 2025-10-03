"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "Ridham Sood"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing = ChequingAccount(12345, 123, 400, date(2025, 5, 1), 500, 0.02)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing)

# 3b.
print(f"Service Charge: ${chequing.get_service_charge()}")

print()
# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    chequing.deposit(100)
    print(chequing)
except ValueError as e:
    print(e)

print(f"Service Charge: ${chequing.get_service_charge()}")


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
saving = SavingsAccount(12345, 123, 1000, date(2025, 5, 1), 500)


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(saving)
print(f"Service Charge: ${saving.get_service_charge()}")

print()
# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    saving.withdraw(600)
    print(saving)
except ValueError as e:
    print(e)

print(f"Service Charge: ${saving.get_service_charge()}")


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment = InvestmentAccount(12345, 123, 1000, date(2018, 5, 1), 2.00)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment)

print(f"Service Charge: ${investment.get_service_charge()}")


print()
# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_updated = InvestmentAccount(12345, 123, 1000, date(2013, 5, 1), 2.00)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_updated)

print(f"Service Charge: ${investment_updated.get_service_charge()}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing.withdraw(100)
    saving.withdraw(200)
    investment.withdraw(300)
    investment_updated.withdraw(500)
except ValueError as e:
    print(e)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing)
print(f"Calculated Service Charge: ${chequing.get_service_charge()}")
print()
print(saving)
print(f"Calculated Service Charge: ${saving.get_service_charge()}")
print()
print(investment)
print(f"Calculated Service Charge: ${investment.get_service_charge()}")
print()
print(investment_updated)
print(f"Calculated Service Charge: ${investment_updated.get_service_charge()}")
