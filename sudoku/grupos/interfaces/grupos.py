from abc import abstractmethod
from abc import ABCMeta

from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponibles
from sudoku.grupos.interfaces.unicoNumeroPosible import UnicoNumeroPosible
from sudoku.grupos.interfaces.numerosFaltantes import NumerosFaltantes
from sudoku.grupos.interfaces.vecinos import Vecinos
from sudoku.grupos.interfaces.matriz import Matriz

class Grupo(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.matriz: Matriz
        self.vecinos: Vecinos
        self.numerosFaltantes: NumerosFaltantes
        self.espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponibles
        self.unicoNumeroPosible: UnicoNumeroPosible

    @abstractmethod
    def guardarGruposVecinosEnFila(self, vecinos: list):
        pass
    
    @abstractmethod
    def guardarGruposVecinosEnColumna(self, vecinos: list):
        pass
    
    @abstractmethod
    def guardarMatriz(self, matriz):
        pass
    
    @abstractmethod
    def limpiarNumerosDisponiblesEnVecinos(self):
        pass
    
    @abstractmethod
    def buscarNumeros(self):
        pass
    
    @abstractmethod
    def verificarNumero(self):
        pass       
    
    @abstractmethod
    def H1(self):
        pass
    
    @abstractmethod
    def ponerNumeroEnMatriz(self, number: int, row: int, column: int):
        pass
    
    @abstractmethod
    def eliminarDeNumerosFaltantes(self, number: int):
        pass
    
    @abstractmethod
    def eliminarMatrizDeNumeroFaltante(self, number: int):
        pass
    
    @abstractmethod
    def H7(self):
        pass
    
    @abstractmethod
    def H8(self):
        pass
    
    @abstractmethod
    def H9(self):
        pass
    
    @abstractmethod
    def esUnicoNumeroPosibleEnGrupo(self):    
        pass
    
    @abstractmethod
    def esUnicoNumeroPosibleEnCasilla(self):
        pass
    
    @abstractmethod
    def esUnicoNumeroPosibleEnFila(self):
       pass
    
    @abstractmethod
    def esUnicoNumeroPosibleEnColumna(self):
        pass
    
    @abstractmethod
    def ponerNumero(self):
        pass