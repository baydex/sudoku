from sudoku.herramientas.utils import *
from sudoku.herramientas.fabricas import *

class Sudoku(object):
    def __init__(self) -> None:
        self.grupos = list()

    def cargarSudoku(self, rutaArchivoSudoku : str) -> None:
        self.grupos = cargarSudokuFact().cargar(rutaArchivoSudoku)

    def resolver(self) -> None:
        self.sudoku = resolverFact().resolver(self.grupos)

    def show(self) -> None:
        showFact().show(self.sudoku)