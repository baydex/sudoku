from abc import abstractmethod
from abc import ABCMeta

from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponiblesInterfaz
from sudoku.grupos.interfaces.vecinos import VecinosInterfaz

class UnicoNumeroPosibleInterfaz(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__numeroVerificado: bool
    
    @abstractmethod        
    def enGrupo(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int) -> None:    
        pass

    @abstractmethod
    def casillaEncontrada(self, fila: int, columna: int) -> bool:
        pass

    @abstractmethod
    def numeroNoVerificado(self) -> bool:
        pass

    @abstractmethod
    def verificarGrupo(self, fila: int, columna: int) -> bool:
        pass

    @abstractmethod
    def enCasilla(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int) -> None:
        pass

    @abstractmethod
    def noHuboCoincidenciasEnOtrosNumeros(self, matrizDeOtrosNumeros: EspaciosDeNumerosDisponiblesInterfaz, fila: int, columna: int) -> bool:
        pass

    @abstractmethod
    def verificarCasilla(self, matrizDeOtrosNumeros: EspaciosDeNumerosDisponiblesInterfaz, fila: int, columna: int) -> bool:
        pass

    @abstractmethod
    def enFila(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int, vecinos: VecinosInterfaz) -> None:
        pass

    @abstractmethod
    def noHuboCoincidenciasEnVecinos(self, fila_columna: int) -> bool:
        pass

    @abstractmethod
    def verificarFilaColumna(self, suma: int, x: int) -> bool | list:
        pass
    
    @abstractmethod
    def enColumna(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int, vecinos: VecinosInterfaz) -> None:
        pass

    @abstractmethod
    def get(self) -> bool:
        pass

    @abstractmethod
    def restaurar(self) -> None:
        pass