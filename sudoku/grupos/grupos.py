

from copy import deepcopy


class Grupo(object):
    def guardarGruposVecinosEnFila(self,vecinos):
        self.gruposVecinosEnFila = vecinos
    
    def guardarGruposVecinosEnColumna(self,vecinos):
        self.gruposVecinosEnColumna = vecinos

    def guardarMatriz(self, matriz):
        self.matriz = matriz

        self.crearNumerosFaltantes()
        
        self.crearEspaciosDeNumerosDisponibles(self.numerosFaltantes, self.matriz)

        self.complete = False
    
    def crearNumerosFaltantes(self):
        self.numerosFaltantes = [i for i in range(1,10)]
        for fila in self.matriz:
            for numero in fila:
                if numero in self.numerosFaltantes:
                    self.numerosFaltantes.remove(numero)

    def crearEspaciosDeNumerosDisponibles(self, missingNumbers, matrix):
        newMatrix = deepcopy(matrix)
        for row in range(3):
            for slot in range(3):
                newMatrix[row][slot] = 1 if newMatrix[row][slot] == 0 else 0  
        emptySlots = {}
        for number in missingNumbers:
            emptySlots[number] = deepcopy(newMatrix)
        self.espaciosDeNumerosDisponibles = emptySlots
    

    def limpiarNumerosDisponibles(self):
        for fila in range(0,3):
            for columna in range(0,3):
                self.numero = self.matriz[fila][columna]
                if self.numero != 0:
                    self.eliminarNumeroDeDisponiblesEnVecinos(fila,columna)

    def eliminarNumeroDeDisponiblesEnVecinos(self,fila,columna):
        self.eliminarNumeroEnFilaDeVecinos(self.numero, fila)
        self.eliminarNumeroEnColumnaDeVecinos(self.numero, columna)

    def buscarNumeros(self):
        for numeroFaltante in self.numerosFaltantes:
            self.numeroFaltante = numeroFaltante
            self.verificarNumero()
            if self.numeroVerificado != False:
                print(self.matriz)
                print(self.numeroFaltante)
                print(self.numeroVerificado)
                print("/-------")
                self.ponerNumero()

    def verificarNumero(self):
        self.numeroVerificado = False
        self.existeUnaCasillaParaNumero()
        self.esUnicoNumeroPosibleEnGrupo()
        self.esUnicoNumeroPosibleEnFila()
        self.esUnicoNumeroPosibleEnColumna()
        

    def H1(self):
        # 1 Obtener numeros faltantes

        pass
    
    def ponerNumeroEnMatriz(self, number, row, column):
        # 2 Poner un numero en la matriz real
        self.matriz[row][column] = number

    def eliminarDeNumerosFaltantes(self, number):
        # 3 Eliminar numero de numeros faltantes
        self.numerosFaltantes.remove(number)


    def eliminarMatrizDeNumeroFaltante(self, number):
        # 4 Eliminar matriz de numero en los faltantes
        del self.espaciosDeNumerosDisponibles[number]

    def eliminarNumeroEnFilaDeVecinos(self, number, row):
        # 5 Eliminar numero de fila en grupos vecinos
        for vecino in self.gruposVecinosEnFila:
            for column in range(3):
                if number in vecino.espaciosDeNumerosDisponibles:
                    vecino.espaciosDeNumerosDisponibles[number][row][column] = 0

    def eliminarNumeroEnColumnaDeVecinos(self, number, column):
        # 6 Eliminar numero de columna en grupos vecinos
        for vecino in self.gruposVecinosEnColumna:
            for row in range(3):
                if number in vecino.espaciosDeNumerosDisponibles:
                    vecino.espaciosDeNumerosDisponibles[number][row][column] = 0


    def H7(self):
        # 7 Contar opciones disponibles de un numero

        pass

    def H8(self):
        # 8 Las casillas disponibles solo existen en una unica fila?

        pass

    def H9(self):
        # 9 Las casillas disponibles solo existen en una unica columna?

        pass

    def existeUnaCasillaParaNumero(self):    
        # 10 Existe solo 1 casilla disponible para X numero?
        matrizDeNumero = self.espaciosDeNumerosDisponibles[self.numeroFaltante]

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

    def esUnicoNumeroPosibleEnGrupo(self):
        # 11 En alguna de las casillas disponibles es el unico numero posible?
        matrizDeNumero = self.espaciosDeNumerosDisponibles[self.numeroFaltante]
        matrizDeOtrosNumeros = deepcopy(self.espaciosDeNumerosDisponibles)
        del matrizDeOtrosNumeros[self.numeroFaltante]
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

    def esUnicoNumeroPosibleEnFila(self):
        # 12 El numero es el unico posible en su fila?
        matrizDeNumero = self.espaciosDeNumerosDisponibles[self.numeroFaltante]
        for fila in range(3):
            suma = deepcopy(matrizDeNumero[fila])
            for vecino in self.gruposVecinosEnFila:
                if self.numeroFaltante in vecino.espaciosDeNumerosDisponibles:
                   suma+= vecino.espaciosDeNumerosDisponibles[self.numeroFaltante][fila]
            if sum(suma) == 1:
                for columna in range(3):
                    if matrizDeNumero[fila][columna] == 1:
                        if self.numeroVerificado == False:
                            return [fila, columna]


    def esUnicoNumeroPosibleEnColumna(self):
        # 13 El numero es el unico posible en su columna?
        matrizDeNumero = self.espaciosDeNumerosDisponibles[self.numeroFaltante]
        for columna in range(3):
            suma =  matrizDeNumero[0][columna] + matrizDeNumero[1][columna] + matrizDeNumero[2][columna]
            for vecino in self.gruposVecinosEnColumna:
                if self.numeroFaltante in vecino.espaciosDeNumerosDisponibles:
                    suma+= vecino.espaciosDeNumerosDisponibles[self.numeroFaltante][0][columna]
                    suma+= vecino.espaciosDeNumerosDisponibles[self.numeroFaltante][1][columna]
                    suma+= vecino.espaciosDeNumerosDisponibles[self.numeroFaltante][2][columna]
            if suma == 1:
                for fila in range(3):
                    if matrizDeNumero[fila][columna] == 1:
                        if self.numeroVerificado == False:
                            return [fila, columna]
        
    def ponerNumero(self):
        self.ponerNumeroEnMatriz(self.numeroFaltante, self.numeroVerificado[0], self.numeroVerificado[1])
        self.eliminarDeNumerosFaltantes(self.numeroFaltante)
        self.eliminarMatrizDeNumeroFaltante(self.numeroFaltante)
        self.eliminarNumeroEnFilaDeVecinos(self.numeroFaltante, self.numeroVerificado[0])
        self.eliminarNumeroEnColumnaDeVecinos(self.numeroFaltante, self.numeroVerificado[1])

    def verEspaciosDeNumerosDisponibles(self):
        for numero in self.espaciosDeNumerosDisponibles:
            print(numero)
            for espacio in self.espaciosDeNumerosDisponibles[numero]:
                print(espacio)
            print("/////////")