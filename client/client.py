"""This file contains the information of the client."""

__name__ = "Ridham Sood"
__version__ = "1.1.0"

from email_validator import EmailNotValidError, validate_email
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    """Initializes a client object."""

    def __init__(self, client_number:int, first_name:str, last_name: str,
                 email_address:str):
        """Initializes the init function.
        
        args:
            client_number: The number of the client.
            first_name: The first name of the client.
            last_name: The last name of the client.
            email_address: The email address of the client.
        
        Raises:
            Valueerror: It raises an exception if first name and last 
                        name is blank.
            Valueerror: It raises an exception if the client number is
                        not if int type.
            Valueerror: It raises an exception if email address is not
                        valid.
        
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an int type.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name should not be blank.")
        
        if validate_email(email_address):
            self.__email_address = email_address
        else:
            raise EmailNotValidError("Email address should be in the correct format.")
        
    @property
    def client_number(self) -> int:
        """This helps to access the client number anywhere.
        
        Return:
        int: Returns the client number
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """This helps to access the first name of the client anywhere.
        
        Return:
        str: Returns the first name of the client
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """This helps to access the last name of the client anywhere.
        
        Return:
        str: Returns the last name of the client.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """This helps to access the email address of the client anywhere.
        
        Return:
        str: Returns the email address of the client
        """
        return self.__email_address
    
    def __str__(self) -> str:
        """This method returns the formatted string.
        
        Return:
        str: Return the formatted string.
        """
        return(f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}")
        
    def update(self, message: str) -> None:
        """This method updates the message.
        
        Args
        message(str): Represents the message to be shown.
        """
        subject = f"Alert: Unusual Activity: {datetime.now()}"
        message = (f"Notification for {self.__client_number}: {self.__first_name}"
                    +f"{self.__last_name}: {message}")
        
        simulate_send_email(self.email_address, subject, message)
