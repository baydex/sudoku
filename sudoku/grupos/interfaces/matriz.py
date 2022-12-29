from abc import abstractmethod
from abc import ABCMeta

class MatrizInterfaz(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.__matriz: list

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

    @abstractmethod
    def show(self, etiqueta: str):
        pass

    @abstractmethod
    def getFila(self, fila: int) -> list:
        pass

    @abstractmethod
    def setFila(self, fila: int, value: list) -> list:
        pass

    @abstractmethod
    def getColumna(self, columna: int) -> list:
        pass

    @abstractmethod
    def setColumna(self, columna: int, value: list) -> list:
        pass

    @abstractmethod
    def transponer(self) -> None:
        pass