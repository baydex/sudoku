from abc import abstractmethod
from abc import ABCMeta

from sudoku.interfaces.cargarSudoku import cargarSudokuInterfaz
from sudoku.interfaces.resolver import ResolverInterfaz
from sudoku.interfaces.show import ShowInterfaz

class SudokuInterfaz(metaclass=ABCMeta):
    def __init__(self) -> None:
        
        self.grupos: list
        self.CargarSudoku: cargarSudokuInterfaz
        self.Resolver: ResolverInterfaz
        self.Show: ShowInterfaz
    
    @abstractmethod
    def cargarSudoku(self, rutaArchivoSudoku : str) -> None:
        pass
    
    @abstractmethod
    def resolver(self) -> None:
        pass
    
    @abstractmethod
    def show(self) -> None:
        pass