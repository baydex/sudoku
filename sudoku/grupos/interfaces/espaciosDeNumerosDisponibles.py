from abc import abstractmethod
from abc import ABCMeta

from sudoku.grupos.interfaces.matriz import MatrizInterfaz

class EspaciosDeNumerosDisponiblesInterfaz(metaclass=ABCMeta):
    
    def __init__(self) -> None:
        self.__espaciosDeNumerosDisponibles: dict

    @abstractmethod    
    def crear(self, numerosFaltantes: list, matrix: list) -> None:
        pass

    @abstractmethod
    def generarMatrizInicial(self, matriz: list) -> list:
        pass

    @abstractmethod
    def guardarMatricesIniciales(self, numerosFaltantes: list, matrizInicial: list) -> None:
        pass

    @abstractmethod            
    def get(self) -> dict:
        pass

    @abstractmethod    
    def set(self, value: dict) -> None:
        pass

    @abstractmethod    
    def remove(self, value: int) -> None:
        pass

    @abstractmethod    
    def contieneNumero(self, numero: int) -> bool:
        pass

    @abstractmethod    
    def setConPosicion(self, numero: int, fila: int, columna: int, valor: int) -> None:
        pass

    @abstractmethod    
    def getConPosicion(self, numero: int, fila: int, columna: int) -> int:
        pass

    @abstractmethod
    def limpiarFila(self, numero: int, fila: int) -> None:
        pass

    @abstractmethod
    def limpiarColumna(self, numero: int, columna: int) -> None:
        pass

    @abstractmethod
    def getMatrizDeNumero(self, numero: int) -> MatrizInterfaz:
        pass