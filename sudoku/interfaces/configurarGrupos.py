from abc import abstractmethod
from abc import ABCMeta

class ConfigurarGrupos(metaclass=ABCMeta):
    def __init__(self, grupos: list) -> None:
        self.__grupos: list

    @abstractmethod
    def configurar(self) -> list:
        pass

    @abstractmethod
    def separarSudokuEnGrupos(self) -> None:
        pass

    @abstractmethod
    def guardarVecinosDeGrupos(self) -> None:
        pass

    @abstractmethod    
    def limpiarNumerosDisponiblesDeGrupos(self) -> None:
        pass
