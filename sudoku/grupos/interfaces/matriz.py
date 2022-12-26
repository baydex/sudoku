from abc import abstractmethod
from abc import ABCMeta

class MatrizInterfaz(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.matriz = list()

    @abstractmethod
    def set(self, matriz: list) -> None:
        pass

    @abstractmethod
    def get(self) -> list:
        pass

    @abstractmethod    
    def setConPosicion(self, x: int, y: int, numero: int) -> None:
        pass

    @abstractmethod
    def getConPosicion(self, x: int, y: int) -> int:
        pass