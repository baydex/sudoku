from abc import abstractmethod
from abc import ABCMeta

class cargarSudokuInterfaz(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__grupos: list   

    @abstractmethod
    def cargar(self, rutaArchivoSudoku : str) -> list:
        pass

    @abstractmethod
    def _cargarArchivoFuente(self) -> None:
        pass
