import json
from sudoku.interfaces.cargarSudoku import cargarSudokuInterfaz


class cargarSudoku(cargarSudokuInterfaz):
    def __init__(self) -> None:
        self.__grupos = list()   

    def cargar(self, rutaArchivoSudoku : str) -> list:
        self._rutaArchivoSudoku = rutaArchivoSudoku
        self._cargarArchivoFuente()
        return self.__grupos

    def _cargarArchivoFuente(self) -> None:
        archivoSudoku = open(self._rutaArchivoSudoku,"r")
        self.__grupos = json.load(archivoSudoku)
        archivoSudoku.close()

    