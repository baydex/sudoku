from sudoku.grupos.interfaces.numerosFaltantes import NumerosFaltantesInterfaz

class NumerosFaltantes(NumerosFaltantesInterfaz):
    
    def __init__(self) -> None:
        self.__numerosFaltantes = list()

    def crear(self, matriz: list) -> None:
        self.__numerosFaltantes = [i for i in range(1,10)]
        for fila in matriz:
            for numero in fila:
                if numero in self.__numerosFaltantes:
                    self.__numerosFaltantes.remove(numero)
    
    def get(self) -> list:
        return self.__numerosFaltantes

    def set(self, value: list) -> None:
        self.__numerosFaltantes = value

    def remove(self, value: int) -> None:
        self.__numerosFaltantes.remove(value)

    

    

    