import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.herramientas.vecinos import Vecinos


class Test_Vecinos(unittest.TestCase):

    def test_vecinos(self):
        self.vecinos = Vecinos()

        self.setFila()
        self.getFila()
        self.setColumna()
        self.getColumna()
        self.limpiarNumerosDisponibles()
        self.eliminarNumeroDeDisponibles()
        self.eliminarNumeroEnFila()
        self.eliminarNumeroEnColumna()

    def objetoInicializado(self):
        self.assertIsInstance(self.vecinos.getFila(), list)
        self.assertIsInstance(self.vecinos.getColumna(), list)

        self.assertEqual(self.vecinos.getFila(), list())
        self.assertEqual(self.vecinos.getColumna(), list())

    def setFila(self):
        pass
    
    def getFila(self):
        pass
        
    def setColumna(self):
        pass
        
    def getColumna(self):
        pass
    
    def limpiarNumerosDisponibles(self):
        pass
        
    def eliminarNumeroDeDisponibles(self):
        pass

    def eliminarNumeroEnFila(self):
        pass
    
    def eliminarNumeroEnColumna(self):
        pass










if __name__ == '__main__':
    unittest.main()