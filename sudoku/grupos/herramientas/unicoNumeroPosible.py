from sudoku.grupos.interfaces.unicoNumeroPosible import UnicoNumeroPosibleInterfaz
from sudoku.grupos.interfaces.grupos import GrupoInterfaz

from copy import deepcopy

class UnicoNumeroPosible(UnicoNumeroPosibleInterfaz):

    def __init__(self) -> None:
        self.numeroVerificado = False
        
    def enGrupo(self, espaciosDeNumerosDisponibles, numeroFaltante):    
        # 10 Existe solo 1 casilla disponible para X numero?
        matrizDeNumero = espaciosDeNumerosDisponibles.get()[numeroFaltante]

        conteoDePosiblesCasillas = 0
        filaCasilla = columnaCasilla = None

        for fila in range(3):
            for columna in range(3):
                if matrizDeNumero[fila][columna] == 1:
                    conteoDePosiblesCasillas += 1
                    filaCasilla = fila
                    columnaCasilla = columna

        if conteoDePosiblesCasillas == 1:
            if self.numeroVerificado == False:
                self.numeroVerificado = [filaCasilla, columnaCasilla]

    def enCasilla(self, espaciosDeNumerosDisponibles, numeroFaltante):
        # 11 En alguna de las casillas disponibles es el unico numero posible?
        matrizDeNumero = espaciosDeNumerosDisponibles.get()[numeroFaltante]
        matrizDeOtrosNumeros = deepcopy(espaciosDeNumerosDisponibles.get())
        del matrizDeOtrosNumeros[numeroFaltante]
        for fila in range(3):
            for columna in range(3):
                if matrizDeNumero[fila][columna] == 1:
                    coincidencias = 0
                    for otroNumero in matrizDeOtrosNumeros:
                        if matrizDeOtrosNumeros[otroNumero][fila][columna] == 1:
                            coincidencias+=1
                    if coincidencias == 0:
                        if self.numeroVerificado == False:
                            self.numeroVerificado = [fila,columna]

    def enFila(self, espaciosDeNumerosDisponibles, numeroFaltante, vecinos):
        # 12 El numero es el unico posible en su fila?
        matrizDeNumero = espaciosDeNumerosDisponibles.get()[numeroFaltante]
        for fila in range(3):
            suma = deepcopy(matrizDeNumero[fila])
            for vecino in vecinos.getFila():
                vecino: GrupoInterfaz
                if numeroFaltante in vecino.espaciosDeNumerosDisponibles.get():
                   suma+= vecino.espaciosDeNumerosDisponibles.get()[numeroFaltante][fila]
            if sum(suma) == 1:
                for columna in range(3):
                    if matrizDeNumero[fila][columna] == 1:
                        if self.numeroVerificado == False:
                            self.numeroVerificado = [fila, columna]


    def enColumna(self, espaciosDeNumerosDisponibles, numeroFaltante, vecinos):
        # 13 El numero es el unico posible en su columna?
        matrizDeNumero = espaciosDeNumerosDisponibles.get()[numeroFaltante]
        for columna in range(3):
            suma =  matrizDeNumero[0][columna] + matrizDeNumero[1][columna] + matrizDeNumero[2][columna]
            for vecino in vecinos.getColumna():
                vecino: GrupoInterfaz
                if numeroFaltante in vecino.espaciosDeNumerosDisponibles.get():
                    suma+= vecino.espaciosDeNumerosDisponibles.getConPosicion(numeroFaltante, 0, columna)
                    suma+= vecino.espaciosDeNumerosDisponibles.getConPosicion(numeroFaltante, 1, columna)
                    suma+= vecino.espaciosDeNumerosDisponibles.getConPosicion(numeroFaltante, 2, columna)
            if suma == 1:
                for fila in range(3):
                    if matrizDeNumero[fila][columna] == 1:
                        if self.numeroVerificado == False:
                            self.numeroVerificado = [fila, columna]