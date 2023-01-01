from sudoku.grupos.interfaces.vecinos import Vecinos
from sudoku.grupos.interfaces.matriz import Matriz
from sudoku.grupos.interfaces.grupos import Grupo

class VecinosImp(Vecinos):
    def __init__(self) -> None:
        self.__fila = list()
        self.__columna = list()

    def setFila(self, vecinos):
        self.__fila = vecinos
    
    def getFila(self) -> list:
        return self.__fila

    def setColumna(self, vecinos : list) -> None:
        self.__columna = vecinos
    
    def getColumna(self) -> list:
        return self.__columna

    def limpiarNumerosDisponibles(self, matriz : Matriz) -> None:
        for fila in range(0,3):
            for columna in range(0,3):
                numero = matriz.getConPosicion(fila, columna)
                if numero != 0:
                    self.eliminarNumeroDeDisponibles(numero,fila,columna)
    
    def eliminarNumeroDeDisponibles(self, numero, fila: int, columna: int) -> None:
        self.eliminarNumeroEnFila(numero, fila)
        self.eliminarNumeroEnColumna(numero, columna)


    def eliminarNumeroEnFila(self, numero: int, row: int) -> None:
        # 5 Eliminar numero de fila en grupos vecinos
        for vecino in self.getFila():
            vecino: Grupo
            if vecino.espaciosDeNumerosDisponibles.contieneNumero(numero):
                vecino.espaciosDeNumerosDisponibles.limpiarFila(numero, row)

    def eliminarNumeroEnColumna(self, numero: int, column: int) -> None:
        # 6 Eliminar numero de columna en grupos vecinos
        for vecino in self.getColumna():
            vecino: Grupo
            if vecino.espaciosDeNumerosDisponibles.contieneNumero(numero):
                vecino.espaciosDeNumerosDisponibles.limpiarColumna(numero, column)