from abc import abstractmethod
from abc import ABCMeta

from sudoku.grupos.interfaces.matriz import MatrizInterfaz

class VecinosInterfaz(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.fila: list
        self.columna: list

    @abstractmethod
    def setFila(self, vecinos : list) -> None:
        pass
    
    @abstractmethod
    def getFila(self) -> list:
        pass
    
    @abstractmethod    
    def setColumna(self, vecinos : list) -> None:
        pass
    
    @abstractmethod    
    def getColumna(self) -> list:
        pass
    
    @abstractmethod
    def limpiarNumerosDisponibles(self, matriz : MatrizInterfaz) -> None:
        pass
    
    @abstractmethod    
    def eliminarNumeroDeDisponibles(self,numero, fila: int, columna: int) -> None:
        pass

    @abstractmethod
    def eliminarNumeroEnFila(self, numero: int, row: int) -> None:
        pass
    
    @abstractmethod
    def eliminarNumeroEnColumna(self, numero: int, column: int) -> None:
        pass