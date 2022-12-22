from copy import deepcopy


class EspaciosDeNumerosDisponibles:
    def __init__(self) -> None:
        self.espaciosDeNumerosDisponibles = dict()

    def crear(self, missingNumbers, matrix):
        newMatrix = deepcopy(matrix)
        for row in range(3):
            for slot in range(3):
                newMatrix[row][slot] = 1 if newMatrix[row][slot] == 0 else 0  
        emptySlots = {}
        for number in missingNumbers:
            emptySlots[number] = deepcopy(newMatrix)
        self.espaciosDeNumerosDisponibles = emptySlots
        
    
    def get(self):
        return self.espaciosDeNumerosDisponibles
    
    def set(self, value):
        self.espaciosDeNumerosDisponibles = value
    
    def remove(self, value):
        del self.espaciosDeNumerosDisponibles[value]

    def contieneNumero(self, numero: int) -> bool:
        return numero in self.get()
    
    def setConPosicion(self, numero, fila, columna, valor):
        self.espaciosDeNumerosDisponibles[numero][fila][columna] = valor
    
    def getConPosicion(self, numero, fila, columna):
        return self.espaciosDeNumerosDisponibles[numero][fila][columna]