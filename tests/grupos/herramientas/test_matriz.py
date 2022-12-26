from copy import deepcopy
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

        self.MatrizVacia()
        self.set()
        self.get()
        self.setConPosicion()

    def MatrizVacia(self):
        self.assertIsInstance(self.matriz.get(), list)
        self.assertEqual(self.matriz.get(), list())


    def set(self):

        self.matriz.set(self.matrizEjemplo)
        self.assertIsInstance(self.matriz.get(), list)
        self.assertEqual(self.matriz.get(), self.matrizEjemplo)

    def get(self):
        self.assertIsInstance(self.matriz.getConPosicion(0,0), int)

    def setConPosicion(self):
        self.matriz.setConPosicion(0,0,0)

        self.assertNotEqual(self.matriz.get(), self.matrizEjemplo)
        self.assertEqual(self.matriz.get(), self.matrizEjemploModificada)

if __name__ == '__main__':
    unittest.main()