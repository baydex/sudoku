from abc import abstractmethod
from abc import ABCMeta

from sudoku.interfaces.cargarSudoku import cargarSudoku
from sudoku.interfaces.resolver import Resolver
from sudoku.interfaces.show import Show

class Sudoku(metaclass=ABCMeta):
    def __init__(self) -> None:
        
        self.__grupos: list
        self.__CargarSudoku: cargarSudoku
        self.__Resolver: Resolver
        self.__Show: Show
    
    @abstractmethod
    def cargarSudoku(self, rutaArchivoSudoku : str) -> None:
        pass
    
    @abstractmethod
    def resolver(self) -> None:
        pass
    
    @abstractmethod
    def show(self) -> None:
        pass