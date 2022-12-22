from sudoku.grupos.herramientas.matriz import Matriz
class Vecinos:
    def __init__(self) -> None:
        self.fila = list()
        self.columna = list()

    def setFila(self, vecinos : list) -> None:
        self.fila = vecinos
    
    def getFila(self) -> list:
        return self.fila

    def setColumna(self, vecinos : list) -> None:
        self.columna = vecinos
    
    def getColumna(self) -> list:
        return self.columna

    def limpiarNumerosDisponibles(self, matriz : Matriz):
        for fila in range(0,3):
            for columna in range(0,3):
                numero = matriz.getConPosicion(fila, columna)
                if numero != 0:
                    self.eliminarNumeroDeDisponibles(numero,fila,columna)
    
    def eliminarNumeroDeDisponibles(self,numero, fila, columna):
        self.eliminarNumeroEnFila(numero, fila)
        self.eliminarNumeroEnColumna(numero, columna)


    def eliminarNumeroEnFila(self, numero, row):
        # 5 Eliminar numero de fila en grupos vecinos
        for vecino in self.getFila():
            for column in range(3):
                if vecino.espaciosDeNumerosDisponibles.contieneNumero(numero):
                    vecino.espaciosDeNumerosDisponibles.setConPosicion(numero, row, column, 0)

    def eliminarNumeroEnColumna(self, numero, column):
        # 6 Eliminar numero de columna en grupos vecinos
        for vecino in self.getColumna():
            for row in range(3):
                if vecino.espaciosDeNumerosDisponibles.contieneNumero(numero):
                    vecino.espaciosDeNumerosDisponibles.setConPosicion(numero, row, column, 0)