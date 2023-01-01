from copy import deepcopy
import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.grupos import GrupoImp

from sudoku.grupos.herramientas.vecinos import VecinosImp
from sudoku.grupos.herramientas.matriz import MatrizImp
from sudoku.grupos.interfaces.matriz import Matriz
from sudoku.grupos.interfaces.grupos import Grupo


class Test_Vecinos(unittest.TestCase):

    def test_vecinos(self):
        self.vecinos = VecinosImp()

        self.objetoInicializado()
        self.setFila()
        self.getFila()
        self.setColumna()
        self.getColumna()
        self.eliminarNumeroEnFila()
        self.eliminarNumeroEnColumna()
        self.eliminarNumeroDeDisponibles()
        self.limpiarNumerosDisponibles()

    def objetoInicializado(self):
        fila = self.vecinos.getFila()
        columna = self.vecinos.getColumna()

        self.assertIsInstance(fila, list)
        self.assertIsInstance(columna, list)

        self.assertEqual(self.vecinos.getFila(), list())
        self.assertEqual(self.vecinos.getColumna(), list())

    def setFila(self):
        grupo1 = GrupoImp()
        matriz1 = [[7, 1, 0], [8, 0, 6], [0, 0, 5]]
        grupo1.guardarMatriz(matriz1)

        grupo2 = GrupoImp()
        matriz2 = [[0, 0, 0], [5, 0, 0], [0, 0, 7]]
        grupo2.guardarMatriz(matriz2)

        vecinos = [grupo1, grupo2]

        self.vecinos.setFila(vecinos)

    def getFila(self):
        fila = self.vecinos.getFila()
        vecino: Grupo = fila[0]
        self.assertIsInstance(fila, list)
        self.assertIsInstance(vecino, Grupo)
        self.assertEqual(vecino.matriz.get(), [[7, 1, 0], [8, 0, 6], [0, 0, 5]])
        
    def setColumna(self):
        grupo1 = GrupoImp()
        matriz1 = [[0, 1, 0], [3, 9, 0], [0, 0, 0]]
        grupo1.guardarMatriz(matriz1)

        grupo2 = GrupoImp()
        matriz2 = [[0, 0, 1], [0, 0, 3], [2, 4, 0]]
        grupo2.guardarMatriz(matriz2)

        vecinos = [grupo1, grupo2]

        self.vecinos.setColumna(vecinos)
        
    def getColumna(self):
        columna = self.vecinos.getColumna()
        self.assertIsInstance(columna, list)
        self.assertIsInstance(columna[0], Grupo)
        self.assertEqual(columna[0].matriz.get(), [[0, 1, 0], [3, 9, 0], [0, 0, 0]])
    
    def limpiarNumerosDisponibles(self):
        matriz = MatrizImp()

        vecinos = self.vecinos.getFila() + self.vecinos.getColumna()
        
        nuevaMatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        matriz.set(nuevaMatriz)
        matricesIguales = True

        self.compararTodasLasMatrices(matriz, vecinos, matricesIguales)
        
        nuevaMatriz = [[1, 3, 6], [4, 5, 2], [7, 8, 9]]
        matriz.set(nuevaMatriz)
        matricesIguales = False

        self.compararTodasLasMatrices(matriz, vecinos, matricesIguales)
    
    def compararTodasLasMatrices(self, matriz, vecinos, matricesIguales):
        
        respaldo = self.recopilarMatrices(vecinos)

        self.vecinos.limpiarNumerosDisponibles(matriz)

        modificado = self.recopilarMatrices(vecinos)

        for posicion in range(len(respaldo)):
            matrizRespaldada = respaldo[posicion][1].get()
            matrizModificada = modificado[posicion][1].get()
            if matricesIguales:
                self.assertEqual(matrizRespaldada, matrizModificada)
            else:
                self.assertNotEqual(matrizRespaldada, matrizModificada)


    def eliminarNumeroEnFila(self):
        numero = 2
        fila = 0

        respaldoVecinos = self.recopilarMatrices(self.vecinos.getFila())
          
        self.vecinos.eliminarNumeroEnFila(numero, fila)

        modificadoVecinos = self.recopilarMatrices(self.vecinos.getFila())
        
        self.compararDiferenciasEnMatrices(respaldoVecinos, modificadoVecinos, numero)

        self.comprobarFila_Columna(numero, fila, False)

    def comprobarFila_Columna(self, numero, fila_columna, esColumna):
        if esColumna :
            vecinos = self.vecinos.getColumna() 
        else:
            vecinos = self.vecinos.getFila()
        for vecino in vecinos:
            vecino: Grupo
            if vecino.espaciosDeNumerosDisponibles.contieneNumero(numero):
                matrizVecino = vecino.espaciosDeNumerosDisponibles.getMatrizDeNumero(numero)
                if esColumna:
                    matriz = matrizVecino.getColumna(fila_columna) 
                else:
                    matriz = matrizVecino.getFila(fila_columna)
                self.assertEqual(matriz, [0,0,0])

    def recopilarMatrices(self, vecinos):
        recopilado = []
        for vecino in vecinos:
            vecino: Grupo
            for claveDeMatriz in vecino.espaciosDeNumerosDisponibles.get():
                espacio: Matriz = vecino.espaciosDeNumerosDisponibles.getMatrizDeNumero(claveDeMatriz)
                recopilado.append([claveDeMatriz, deepcopy(espacio)])
        return recopilado

    def compararDiferenciasEnMatrices(self, respaldo, modificado, numero):
        for posicion in range(len(respaldo)):
            matriz1 = respaldo[posicion][1]
            matriz2 = modificado[posicion][1]
            matriz1: Matriz
            matriz2: Matriz
            if respaldo[posicion][0] == numero:
                self.assertNotEqual(matriz1.get(), matriz2.get())
            else:
                self.assertEqual(matriz1.get(), matriz2.get())

    def eliminarNumeroEnColumna(self):

        numero = 2
        columna = 0

        respaldoVecinos = self.recopilarMatrices(self.vecinos.getColumna())
          
        self.vecinos.eliminarNumeroEnColumna(numero, columna)

        modificadoVecinos = self.recopilarMatrices(self.vecinos.getColumna())

        self.compararDiferenciasEnMatrices(respaldoVecinos, modificadoVecinos, numero)

        self.comprobarFila_Columna(numero, columna, True)

    def eliminarNumeroDeDisponibles(self):
        numero = 8
        fila = 0
        columna = 0
        self.vecinos.eliminarNumeroDeDisponibles(numero, fila, columna)

        self.comprobarNumeroDeDisponibles(numero, fila, False)
        self.comprobarNumeroDeDisponibles(numero, columna, True)
    
    def comprobarNumeroDeDisponibles(self, numero, fila_columna, esColumna):
        if esColumna: 
            vecinos = self.vecinos.getColumna() 
        else:
            vecinos = self.vecinos.getFila()
        for vecino in vecinos:
            vecino: Grupo
            if vecino.espaciosDeNumerosDisponibles.contieneNumero(numero):
                matriz = vecino.espaciosDeNumerosDisponibles.getMatrizDeNumero(numero)
                if esColumna: 
                    columna_filaDeMatriz = matriz.getColumna(fila_columna) 
                else:
                    columna_filaDeMatriz = matriz.getFila(fila_columna)
                matrizEsperada = [0,0,0]
                self.assertEqual(columna_filaDeMatriz, matrizEsperada)

if __name__ == '__main__':
    unittest.main()