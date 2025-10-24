"""This file contains the interface which will notify the changes."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """This class constructs an interface which will notify the changes
    made in the subject."""

    @abstractmethod
    def update(self, message: str) -> None:
        """This method will update the changes.
        
        Args:
        message(str): Represents the message to be updated
        """

        pass
