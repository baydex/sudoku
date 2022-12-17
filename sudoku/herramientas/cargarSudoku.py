import json
from sudoku.grupos.grupos import Grupo

class cargarSudoku:
    def __init__(self) -> None:
        self._grupos = list()   

    def cargar(self, rutaArchivoSudoku : str) -> list:
        self._rutaArchivoSudoku = rutaArchivoSudoku
        self._cargarArchivoFuente()
        return self._grupos

    def _cargarArchivoFuente(self) -> None:
        archivoSudoku = open(self._rutaArchivoSudoku,"r")
        self._grupos = json.load(archivoSudoku)
        archivoSudoku.close()

    