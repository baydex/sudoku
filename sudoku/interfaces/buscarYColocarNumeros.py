from abc import abstractmethod
from abc import ABCMeta

class buscarYColocarNumeros(metaclass=ABCMeta):

    def __init__(self,grupos) -> None:
        self.__grupos: list

    @abstractmethod    
    def ejecutar(self) -> list:
        pass
    
    @abstractmethod    
    def guardarNumerosDisponibles(self) -> None:
        pass
    
    @abstractmethod    
    def repetirBusqueda(self) -> None:
        pass
    
    @abstractmethod    
    def progresarEnBuqueda(self) -> None:
        pass
    
    @abstractmethod    
    def verificarProgresoEnBusqueda(self) -> None:
        pass