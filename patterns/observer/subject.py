"""This file contains the class to store the list of observers."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from .observer import Observer

class Subject(ABC):
    """This is the superclass uses to maintain the list of observers and
    notifies the changes or events."""

    def __init__(self) -> None:
        """Initializes the init method.
        """

        self._observer = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """This method attaches the observer to be shown.
        
        Args:
        observer(Observer): Represents the observer to be shown.
        """

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """This method detaches the observer.
        
        Args:
        observer(Observer): Represents the observer to be detached.
        """

        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """This method displays the message to the person.
        
        Args:
        message(str): Represents the message to be shown.
        """

        pass