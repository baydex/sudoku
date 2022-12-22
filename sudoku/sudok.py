from sudoku.herramientas.utils import *
from sudoku.herramientas.fabricas import *

class Sudoku(object):
    def __init__(self) -> None:
        
        self.grupos = list()

        self.CargarSudoku = cargarSudokuFact()
        self.Resolver = resolverFact()
        self.Show = showFact()

    def cargarSudoku(self, rutaArchivoSudoku : str) -> None:
        self.grupos = self.CargarSudoku.cargar(rutaArchivoSudoku)

    def resolver(self) -> None:
        self.sudoku = self.Resolver.resolver(self.grupos)

    def show(self) -> None:
        self.Show.show(self.sudoku)