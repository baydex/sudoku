from abc import abstractmethod
from abc import ABCMeta

class ResolverInterfaz(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__grupos: list
    
    @abstractmethod
    def resolver(self, grupos: list) -> list:
        pass
    
    @abstractmethod
    def configurarGrupos(self) -> None:
        pass
    
    @abstractmethod
    def buscarYColocarNumeros(self) -> None:
        pass