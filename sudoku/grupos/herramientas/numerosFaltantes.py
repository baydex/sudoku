from copy import deepcopy
from sudoku.grupos import grupos

class NumerosFaltantes:
    def __init__(self) -> None:
        pass

    def crear(self, matriz):
        numerosFaltantes = [i for i in range(1,10)]
        for fila in matriz:
            for numero in fila:
                if numero in numerosFaltantes:
                    numerosFaltantes.remove(numero)
        return numerosFaltantes

    def crearEspaciosDeNumerosDisponibles(self, missingNumbers, matrix):
        newMatrix = deepcopy(matrix)
        for row in range(3):
            for slot in range(3):
                newMatrix[row][slot] = 1 if newMatrix[row][slot] == 0 else 0  
        emptySlots = {}
        for number in missingNumbers:
            emptySlots[number] = deepcopy(newMatrix)
        espaciosDeNumerosDisponibles = emptySlots
        return espaciosDeNumerosDisponibles
    

    def limpiarNumerosDisponibles(self, this):
        for fila in range(0,3):
            for columna in range(0,3):
                numero = this.matriz[fila][columna]
                if numero != 0:
                    this.eliminarNumeroDeDisponiblesEnVecinos(numero, fila,columna)
                    return this.gruposVecinosEnColumna, this.gruposVecinosEnFila

    

    