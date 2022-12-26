from abc import abstractmethod
from abc import ABCMeta

from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponiblesInterfaz
from sudoku.grupos.interfaces.vecinos import VecinosInterfaz

class UnicoNumeroPosibleInterfaz(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__numeroVerificado: bool
    
    @abstractmethod        
    def enGrupo(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int):    
        pass
    
    @abstractmethod
    def enCasilla(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int):
        pass
    
    @abstractmethod
    def enFila(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int, vecinos: VecinosInterfaz):
        pass
    
    @abstractmethod
    def enColumna(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int, vecinos: VecinosInterfaz):
        pass

    @abstractmethod
    def get(self) -> bool:
        pass