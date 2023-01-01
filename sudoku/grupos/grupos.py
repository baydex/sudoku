
from sudoku.grupos.herramientas.numerosFaltantes import NumerosFaltantesImp
from sudoku.grupos.herramientas.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponiblesImp
from sudoku.grupos.herramientas.unicoNumeroPosible import UnicoNumeroPosibleImp
from sudoku.grupos.herramientas.vecinos import VecinosImp
from sudoku.grupos.herramientas.matriz import MatrizImp
from sudoku.grupos.interfaces.grupos import Grupo

from copy import deepcopy


class GrupoImp(Grupo):
    def __init__(self) -> None:
        self.matriz = MatrizImp()
        self.vecinos = VecinosImp()
        self.numerosFaltantes = NumerosFaltantesImp()
        self.espaciosDeNumerosDisponibles = EspaciosDeNumerosDisponiblesImp()
        self.unicoNumeroPosible = UnicoNumeroPosibleImp()

    def guardarGruposVecinosEnFila(self, vecinos : list):
        self.vecinos.setFila(vecinos)
    
    def guardarGruposVecinosEnColumna(self, vecinos : list):
        self.vecinos.setColumna(vecinos)

    def guardarMatriz(self, matriz):

        self.matriz.set(matriz)

        self.numerosFaltantes.crear(self.matriz.get())
        
        self.espaciosDeNumerosDisponibles.crear(self.numerosFaltantes.get(), self.matriz.get())

        self.complete = False

    def limpiarNumerosDisponiblesEnVecinos(self):
        self.vecinos.limpiarNumerosDisponibles(self.matriz)

    def buscarNumeros(self):
        for numeroFaltante in self.numerosFaltantes.get():
            self.numeroFaltante = numeroFaltante
            self.verificarNumero()
            if self.numeroVerificado:
                self.ponerNumero()

    def verificarNumero(self):
        self.numeroVerificado = False
        self.esUnicoNumeroPosibleEnGrupo()
        self.esUnicoNumeroPosibleEnCasilla()
        self.esUnicoNumeroPosibleEnFila()
        self.esUnicoNumeroPosibleEnColumna()
        self.numeroVerificado = self.unicoNumeroPosible.get()
        

    def H1(self):
        # 1 Obtener numeros faltantes
        pass
    
    def ponerNumeroEnMatriz(self, number: int, row: int, column: int):
        # 2 Poner un numero en la matriz real
        self.matriz.setConPosicion(row, column, number)

    def eliminarDeNumerosFaltantes(self, number):
        # 3 Eliminar numero de numeros faltantes
        self.numerosFaltantes.remove(number)


    def eliminarMatrizDeNumeroFaltante(self, number):
        # 4 Eliminar matriz de numero en los faltantes
        self.espaciosDeNumerosDisponibles.remove(number)

    def H7(self):
        # 7 Contar opciones disponibles de un numero

        pass

    def H8(self):
        # 8 Las casillas disponibles solo existen en una unica fila?

        pass

    def H9(self):
        # 9 Las casillas disponibles solo existen en una unica columna?

        pass

    def esUnicoNumeroPosibleEnGrupo(self):    
        # 10 Existe solo 1 casilla disponible para X numero?
        self.unicoNumeroPosible.enGrupo(self.espaciosDeNumerosDisponibles, self.numeroFaltante)

    def esUnicoNumeroPosibleEnCasilla(self):
        # 11 En alguna de las casillas disponibles es el unico numero posible?
        self.unicoNumeroPosible.enCasilla(self.espaciosDeNumerosDisponibles, self.numeroFaltante)

    def esUnicoNumeroPosibleEnFila(self):
        # 12 El numero es el unico posible en su fila?
        self.unicoNumeroPosible.enFila(self.espaciosDeNumerosDisponibles, self.numeroFaltante, self.vecinos)


    def esUnicoNumeroPosibleEnColumna(self):
        # 13 El numero es el unico posible en su columna?
        self.unicoNumeroPosible.enColumna(self.espaciosDeNumerosDisponibles, self.numeroFaltante, self.vecinos)
        
    def ponerNumero(self):
        self.ponerNumeroEnMatriz(self.numeroFaltante, self.numeroVerificado[0], self.numeroVerificado[1])
        self.eliminarDeNumerosFaltantes(self.numeroFaltante)
        self.eliminarMatrizDeNumeroFaltante(self.numeroFaltante)
        self.vecinos.eliminarNumeroEnFila(self.numeroFaltante, self.numeroVerificado[0])
        self.vecinos.eliminarNumeroEnColumna(self.numeroFaltante, self.numeroVerificado[1])
