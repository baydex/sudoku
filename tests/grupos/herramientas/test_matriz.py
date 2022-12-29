import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.herramientas.matriz import Matriz


class Test_Matriz(unittest.TestCase):
    
    def test_matriz(self):
        self.matriz = Matriz()
        self.matrizEjemplo = [
            [1,0,0],
            [0,2,5],
            [3,0,0]
        ]

        self.matrizEjemploModificada = [
            [0,0,0],
            [0,2,5],
            [3,0,0]
        ]

        self.matrizEjemploTranspuesta = [
            [1,0,3],
            [0,2,0],
            [0,5,0]
        ]

        self.MatrizVacia()
        self.set()
        self.get()
        self.setConPosicion()
        self.transponer()
        self.setFila()

    def MatrizVacia(self):
        self.assertIsInstance(self.matriz.get(), list)
        self.assertEqual(self.matriz.get(), list())


    def set(self):

        self.matriz.set(self.matrizEjemplo)

        matriz = self.matriz.get()

        self.assertIsInstance(matriz, list)
        self.assertEqual(matriz, self.matrizEjemplo)

    def get(self):
        self.assertIsInstance(self.matriz.getConPosicion(0,0), int)

    def setConPosicion(self):
        self.matriz.setConPosicion(0,0,0)
        matriz = self.matriz.get()

        self.assertNotEqual(matriz, self.matrizEjemplo)
        self.assertEqual(matriz, self.matrizEjemploModificada)

    def transponer(self):
        self.resetearMatriz()

        self.matriz.set(self.matrizEjemplo)
        self.matriz.transponer()
        self.assertEqual(self.matriz.get(), self.matrizEjemploTranspuesta)

    def getFila(self):
        self.resetearMatriz()
        fila = self.matriz.getFila(0)
        self.assertEqual(fila, [1,0,0])

    def setFila(self):
        self.resetearMatriz()
        nuevaFila = [0,0,0]
        self.matriz.setFila(0, nuevaFila)
        fila = self.matriz.getFila(0)
        self.assertEqual(fila, nuevaFila)

    def getColumna(self):
        self.resetearMatriz()
        columna = self.matriz.getColumna(0)
        self.assertEqual(columna, [1,0,0])

    def setColumna(self):
        self.resetearMatriz()
        nuevaColumna = [0,0,0]
        self.matriz.setFila(0, nuevaColumna)
        columna = self.matriz.getColumna(0)
        self.assertEqual(columna, nuevaColumna)

    def resetearMatriz(self):
        self.matriz.set(self.matrizEjemplo)


if __name__ == '__main__':
    unittest.main()