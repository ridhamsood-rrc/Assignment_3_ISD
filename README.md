# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Ridham Sood

## Assignment

Assignment 1: Develop classes to help the larger system.

Assignment 2: Applying Object-Oriented Design using Abstraction, Polymorphism
and Inheritance.

Assignment 3: Applying the strategy and observer patterns. Adding these
patterns add scalability and simplifies the functionality of the service
charges.

## Encapsulation

The Encapsulation in the BankAccount class was achieved by defining various
functions and methods. Firstly, I defined the private attributes like
__account_number and making it accessible by defining methods and
properties.

## Polymorphism

The Polymorphism helps to call a same function in different ways and
responds differently in different functions. For example, get_service_charge
responded in different ways when called on different functions.

## Strategy Pattern

In this application, the Strategy pattern is used in different ways.
The Strategy Pattern is used to separate the calculation of service
charges from the account classes. By defining a ServiceChargeStrategy
interface and implementing it in OverdraftStrategy, the ChequingAccount
class can dynamically use different charging strategies without altering
its core logic. The same logic goes with InvestAccount and SavingAccount
class as I implemented ManagementFeeStrategy and MinimumBalanceStrategy
respectively.
