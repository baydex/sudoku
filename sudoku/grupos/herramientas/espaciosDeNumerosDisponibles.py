from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponiblesInterfaz
from sudoku.grupos.herramientas.matriz import Matriz
from sudoku.grupos.interfaces.matriz import MatrizInterfaz

from copy import deepcopy

class EspaciosDeNumerosDisponibles(EspaciosDeNumerosDisponiblesInterfaz):
    
    def __init__(self) -> None:
        self.__espaciosDeNumerosDisponibles = dict()

    def crear(self, numerosFaltantes: list, matrix: list) -> None:
        newMatrix = deepcopy(matrix)
        for row in range(3):
            for slot in range(3):
                newMatrix[row][slot] = 1 if newMatrix[row][slot] == 0 else 0  
        emptySlots = {}
        for number in numerosFaltantes:
            matrizNueva = Matriz()
            copia = deepcopy(newMatrix)
            matrizNueva.set(copia)
            emptySlots[number] = matrizNueva
        self.__espaciosDeNumerosDisponibles = emptySlots
        
    def get(self) -> dict:
        return self.__espaciosDeNumerosDisponibles
    
    def set(self, value: dict) -> None:
        self.__espaciosDeNumerosDisponibles = value
    
    def remove(self, value: int) -> None:
        del self.__espaciosDeNumerosDisponibles[value]

    def contieneNumero(self, numero: int) -> bool:
        return numero in self.get()
    
    def setConPosicion(self, numero: int, fila: int, columna: int, valor: int) -> None:
        self.__espaciosDeNumerosDisponibles[numero].setConPosicion(fila,columna,valor)
    
    def getConPosicion(self, numero: int, fila: int, columna: int) -> int:
        return self.__espaciosDeNumerosDisponibles[numero].getConPosicion(fila,columna)

    def limpiarFila(self, numero: int, fila: int) -> None:
        matriz = self.__espaciosDeNumerosDisponibles[numero]
        matriz: MatrizInterfaz
        matriz.setFila(fila, [0,0,0])

    def limpiarColumna(self, numero: int, columna: int) -> None:
        matriz = self.__espaciosDeNumerosDisponibles[numero]
        matriz: MatrizInterfaz
        matriz.setColumna(columna, [0,0,0])

    def getMatrizDeNumero(self, numero: int) -> MatrizInterfaz:
        if(self.contieneNumero(numero)):
            return self.__espaciosDeNumerosDisponibles[numero]
        else:
            raise NameError("Este numero no existe en los espacios de numeros disponibles")