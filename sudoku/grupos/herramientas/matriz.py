from sudoku.grupos.interfaces.matriz import MatrizInterfaz

from copy import deepcopy

class Matriz(MatrizInterfaz):

    def __init__(self) -> None:
        self.__matriz = list()

    def set(self, matriz: list) -> None:
        self.__matriz = deepcopy(matriz)

    def get(self) -> list:
        return self.__matriz
    
    def setConPosicion(self, x: int, y: int, numero: int) -> None:
        self.__matriz[x][y] = numero

    def getConPosicion(self, x: int, y: int) -> int:
        return self.__matriz[x][y]

    def transponer(self):
        transpuesta = deepcopy(self.__matriz)
        for i in range(3):
            for j in range(3):
                transpuesta[j][i] = self.__matriz[i][j]
        self.__matriz = transpuesta

    def show(self, etiqueta: str = ""):
        if etiqueta != "":
            print(etiqueta)
        print("--------")
        for fila in self.__matriz:
            print("|",end="")
            for columna in fila:
                print(columna, end=" ")
            print("|")
        print("--------")

    def getFila(self, fila: int) -> list:
        return self.__matriz[fila]

    def setFila(self, fila: int, value: list) -> list:
        self.__matriz[fila] = value

    def getColumna(self, columna: int) -> list:
        self.transponer()
        resultado = self.getFila(columna)
        self.transponer()
        return resultado

    def setColumna(self, columna: int, value: list) -> list:
        self.transponer()
        self.setFila(columna, value)
        self.transponer()


