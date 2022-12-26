from abc import abstractmethod
from abc import ABCMeta

class ConfigurarGruposInterfaz(metaclass=ABCMeta):
    def __init__(self, grupos: list) -> None:
        self.grupos: list

    @abstractmethod
    def configurar(self) -> list:
        pass

    @abstractmethod
    def _separarSudokuEnGrupos(self) -> None:
        pass

    @abstractmethod
    def guardarVecinosDeGrupos(self) -> None:
        pass

    @abstractmethod    
    def limpiarNumerosDisponiblesDeGrupos(self) -> None:
        pass
