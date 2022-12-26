from abc import abstractmethod
from abc import ABCMeta

class EspaciosDeNumerosDisponiblesInterfaz(metaclass=ABCMeta):
    
    def __init__(self) -> None:
        self.espaciosDeNumerosDisponibles: dict

    @abstractmethod    
    def crear(self, numerosFaltantes: list, matrix: list) -> None:
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