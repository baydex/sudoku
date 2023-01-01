from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponibles
from sudoku.grupos.interfaces.matriz import Matriz

from sudoku.grupos.herramientas.matriz import MatrizImp

from copy import deepcopy

class EspaciosDeNumerosDisponiblesImp(EspaciosDeNumerosDisponibles):
    
    def __init__(self) -> None:
        self.__espaciosDeNumerosDisponibles = dict()

    def crear(self, numerosFaltantes: list, matriz: list) -> None:
        
        self.__espaciosDeNumerosDisponibles = dict()

        matrizInicial = self.generarMatrizInicial(matriz)
        
        self.guardarMatricesIniciales(numerosFaltantes, matrizInicial)
        
    def generarMatrizInicial(self, matriz: list) -> list:
        matrizInicial = deepcopy(matriz)
        for fila in range(3):
            for columna in range(3):
                if matrizInicial[fila][columna] == 0: 
                    matrizInicial[fila][columna] = 1 
                else:  
                    matrizInicial[fila][columna] = 0 
        return matrizInicial

    def guardarMatricesIniciales(self, numerosFaltantes: list, matrizInicial: list) -> None:
        for numero in numerosFaltantes:
            matrizNueva = MatrizImp()
            copia = deepcopy(matrizInicial)
            matrizNueva.set(copia)
            self.__espaciosDeNumerosDisponibles[numero] = matrizNueva

    def get(self) -> dict:
        return self.__espaciosDeNumerosDisponibles
    
    def set(self, value: dict) -> None:
        self.__espaciosDeNumerosDisponibles = value
    
    def remove(self, value: int) -> None:
        del self.__espaciosDeNumerosDisponibles[value]

    def contieneNumero(self, numero: int) -> bool:
        return numero in self.get()
    
    def setConPosicion(self, numero: int, fila: int, columna: int, valor: int) -> None:
        self.getMatrizDeNumero(numero).setConPosicion(fila,columna,valor)
    
    def getConPosicion(self, numero: int, fila: int, columna: int) -> int:
        return self.getMatrizDeNumero(numero).getConPosicion(fila,columna)

    def limpiarFila(self, numero: int, fila: int) -> None:
        matriz = self.getMatrizDeNumero(numero)
        matriz.setFila(fila, [0,0,0])

    def limpiarColumna(self, numero: int, columna: int) -> None:
        matriz = self.getMatrizDeNumero(numero)
        matriz.setColumna(columna, [0,0,0])

    def getMatrizDeNumero(self, numero: int) -> Matriz:
        if(self.contieneNumero(numero)):
            return self.__espaciosDeNumerosDisponibles[numero]
        else:
            raise NameError("Este numero no existe en los espacios de numeros disponibles")