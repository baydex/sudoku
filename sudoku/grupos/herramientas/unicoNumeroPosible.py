from sudoku.grupos.interfaces.unicoNumeroPosible import UnicoNumeroPosibleInterfaz
from sudoku.grupos.interfaces.grupos import GrupoInterfaz
from sudoku.grupos.interfaces.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponiblesInterfaz
from sudoku.grupos.interfaces.vecinos import VecinosInterfaz


from copy import deepcopy

class UnicoNumeroPosible(UnicoNumeroPosibleInterfaz):

    def __init__(self) -> None:
        self.__numeroVerificado = False
        self.__esColumna: bool
        self.__vecinos: VecinosInterfaz
        self.__numeroFaltante: int
        
    def enGrupo(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int) -> None:  
        # 10 Existe solo 1 casilla disponible para X numero?
        self.matrizDeNumero = espaciosDeNumerosDisponibles.getMatrizDeNumero(numeroFaltante)

        conteoDePosiblesCasillas = 0
        conteoDePosiblesCasillas += sum(self.matrizDeNumero.getFila(0))
        conteoDePosiblesCasillas += sum(self.matrizDeNumero.getFila(1))
        conteoDePosiblesCasillas += sum(self.matrizDeNumero.getFila(2))
        
        if conteoDePosiblesCasillas == 1:
            for fila in range(3):
                for columna in range(3):
                    if self.verificarGrupo(fila, columna):
                        self.__numeroVerificado = [fila, columna]

    def casillaEncontrada(self, fila: int, columna: int) -> bool:
        return self.matrizDeNumero.getConPosicion(fila, columna) == 1

    def numeroNoVerificado(self) -> bool:
        return self.__numeroVerificado == False

    def verificarGrupo(self, fila: int, columna: int) -> bool:
        verificacion = False
        if self.casillaEncontrada(fila, columna):
            if self.numeroNoVerificado():
                verificacion = True
        return verificacion

    def enCasilla(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int) -> None:
        # 11 En alguna de las casillas disponibles es el unico numero posible?
        self.matrizDeNumero = espaciosDeNumerosDisponibles.getMatrizDeNumero(numeroFaltante)
        matrizDeOtrosNumeros = deepcopy(espaciosDeNumerosDisponibles)
        matrizDeOtrosNumeros.remove(numeroFaltante)
        for fila in range(3):
            for columna in range(3):
                if self.verificarCasilla(matrizDeOtrosNumeros, fila, columna):
                    self.__numeroVerificado = [fila,columna]

    def noHuboCoincidenciasEnOtrosNumeros(self, matrizDeOtrosNumeros: EspaciosDeNumerosDisponiblesInterfaz, fila: int, columna: int) -> bool:
        verificacion = True
        for otroNumero in matrizDeOtrosNumeros.get():
            if matrizDeOtrosNumeros.getMatrizDeNumero(otroNumero).getConPosicion(fila, columna) == 1:
                verificacion = False
        return verificacion

    def verificarCasilla(self, matrizDeOtrosNumeros: EspaciosDeNumerosDisponiblesInterfaz, fila: int, columna: int) -> bool:
        verificacion = False
        if self.casillaEncontrada(fila, columna):
            if self.noHuboCoincidenciasEnOtrosNumeros(matrizDeOtrosNumeros, fila, columna):
                if self.numeroNoVerificado():
                    verificacion = True
        return verificacion
                    

    def enFila(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int, vecinos: VecinosInterfaz) -> None:
        # 12 El numero es el unico posible en su fila?
        self.matrizDeNumero = espaciosDeNumerosDisponibles.getMatrizDeNumero(numeroFaltante)
        for fila in range(3):
            suma = sum(self.matrizDeNumero.getFila(fila))
            self.__esColumna = False
            self.__vecinos = vecinos
            self.__numeroFaltante = numeroFaltante
            verificacion = self.verificarFilaColumna(suma, fila)
            if verificacion:
                columna = verificacion[0]
                self.__numeroVerificado = [fila, columna]            

    def noHuboCoincidenciasEnVecinos(self, fila_columna: int) -> bool:
        verificacion = True

        listaVecinos = self.__vecinos.getColumna() if self.__esColumna else self.__vecinos.getFila()

        for vecino in listaVecinos:
            vecino: GrupoInterfaz
            if vecino.espaciosDeNumerosDisponibles.contieneNumero(self.__numeroFaltante):
                matrizDeNumeroDeVecino = vecino.espaciosDeNumerosDisponibles.getMatrizDeNumero(self.__numeroFaltante)
                if self.__esColumna:
                    fila_columnaDeMatriz = matrizDeNumeroDeVecino.getColumna(fila_columna)
                else:
                    fila_columnaDeMatriz = matrizDeNumeroDeVecino.getFila(fila_columna)
                suma = sum(fila_columnaDeMatriz)
                if suma != 0:
                    verificacion = False
        return verificacion

    def verificarFilaColumna(self, suma: int, x: int) -> bool | list:
        verificacion = False
        if suma == 1:
            if self.noHuboCoincidenciasEnVecinos(x):
                for y in range(3):
                    if self.__esColumna:
                        fila = y
                        columna = x
                    else:
                        fila = x
                        columna = y

                    if self.casillaEncontrada(fila, columna):
                        if self.numeroNoVerificado():
                            verificacion = [fila] if self.__esColumna else [columna]
        return verificacion

    def enColumna(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponiblesInterfaz, numeroFaltante: int, vecinos: VecinosInterfaz) -> None:
        # 13 El numero es el unico posible en su columna?
        self.matrizDeNumero = espaciosDeNumerosDisponibles.getMatrizDeNumero(numeroFaltante)
        for columna in range(3):
            suma =  sum(self.matrizDeNumero.getColumna(columna))
            self.__esColumna = True
            self.__vecinos = vecinos
            self.__numeroFaltante = numeroFaltante
            verificacion = self.verificarFilaColumna(suma, columna)
            if verificacion:
                fila = verificacion[0]
                self.__numeroVerificado = [fila, columna]

    def get(self) -> bool:
        return self.__numeroVerificado

    def restaurar(self) -> None:
        self.__numeroVerificado = False