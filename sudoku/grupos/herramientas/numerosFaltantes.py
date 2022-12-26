from sudoku.grupos.interfaces.numerosFaltantes import NumerosFaltantesInterfaz

class NumerosFaltantes(NumerosFaltantesInterfaz):
    
    def __init__(self) -> None:
        self.numerosFaltantes = list()

    def crear(self, matriz: list) -> None:
        self.numerosFaltantes = [i for i in range(1,10)]
        for fila in matriz:
            for numero in fila:
                if numero in self.numerosFaltantes:
                    self.numerosFaltantes.remove(numero)
    
    def get(self) -> list:
        return self.numerosFaltantes

    def set(self, value: list) -> None:
        self.numerosFaltantes = value

    def remove(self, value: int) -> None:
        self.numerosFaltantes.remove(value)

    

    

    