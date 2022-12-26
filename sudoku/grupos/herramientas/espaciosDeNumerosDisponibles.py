from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponiblesInterfaz

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
            emptySlots[number] = deepcopy(newMatrix)
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
        self.__espaciosDeNumerosDisponibles[numero][fila][columna] = valor
    
    def getConPosicion(self, numero: int, fila: int, columna: int) -> int:
        return self.__espaciosDeNumerosDisponibles[numero][fila][columna]