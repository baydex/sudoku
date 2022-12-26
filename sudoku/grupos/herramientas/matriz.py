from sudoku.grupos.interfaces.matriz import MatrizInterfaz

from copy import deepcopy

class Matriz(MatrizInterfaz):

    def __init__(self) -> None:
        self.matriz = list()

    def set(self, matriz: list) -> None:
        self.matriz = deepcopy(matriz)

    def get(self) -> list:
        return self.matriz
    
    def setConPosicion(self, x: int, y: int, numero: int) -> None:
        self.matriz[x][y] = numero

    def getConPosicion(self, x: int, y: int) -> int:
        return self.matriz[x][y]



