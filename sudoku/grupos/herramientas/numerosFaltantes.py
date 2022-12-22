from copy import deepcopy
from sudoku.grupos import grupos

class NumerosFaltantes:
    def __init__(self) -> None:
        self.numerosFaltantes = list()

    def crear(self, matriz):
        self.numerosFaltantes = [i for i in range(1,10)]
        for fila in matriz:
            for numero in fila:
                if numero in self.numerosFaltantes:
                    self.numerosFaltantes.remove(numero)
    
    def get(self):
        return self.numerosFaltantes

    def set(self, value):
        self.numerosFaltantes = value

    def remove(self, value):
        self.numerosFaltantes.remove(value)

    

    

    