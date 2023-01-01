from abc import abstractmethod
from abc import ABCMeta

class Show(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def show(self, sudoku: list):
        pass