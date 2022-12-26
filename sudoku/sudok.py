from sudoku.herramientas.fabricas import *
from sudoku.interfaces.sudoku import SudokuInterfaz

class Sudoku(SudokuInterfaz):
    def __init__(self) -> None:
        
        self.__grupos = list()

        self.__CargarSudoku = cargarSudokuFact()
        self.__Resolver = resolverFact()
        self.__Show = showFact()

    def cargarSudoku(self, rutaArchivoSudoku : str) -> None:
        self.__grupos = self.__CargarSudoku.cargar(rutaArchivoSudoku)

    def resolver(self) -> None:
        self.sudoku = self.__Resolver.resolver(self.__grupos)

    def show(self) -> None:
        self.__Show.show(self.sudoku)