import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.herramientas.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponibles
from sudoku.grupos.herramientas.matriz import Matriz
from sudoku.grupos.interfaces.matriz import MatrizInterfaz


class Test_EspaciosDeNumerosDisponibles(unittest.TestCase):
    
    def test_espaciosDeNumerosDisponibles(self):
        self.espaciosDeNumerosDisponibles = EspaciosDeNumerosDisponibles()
        self.generarMatrizInicial()
        self.guardarMatricesIniciales()
        self.crear()
        self.get()
        self.set()
        self.remove()
        self.contieneNumero()
        self.setConPosicion()
        self.getConPosicion()
        self.limpiarFila()
        self.limpiarColumna()
        self.getMatrizDeNumero()

    def crear(self):
        matriz = [
            [0,2,3],
            [4,0,5],
            [0,8,9],
        ]
        matrizEsperada = [
            [1,0,0],
            [0,1,0],
            [1,0,0],
        ]
        self.espaciosDeNumerosDisponibles.crear([1, 6, 7], matriz)
        matrices = self.espaciosDeNumerosDisponibles.get()
        matrizDeNumero: MatrizInterfaz = matrices[1]
        self.assertEqual(len(matrices), 3)
        self.assertIsInstance(matrizDeNumero, MatrizInterfaz)
        self.assertEqual(matrizDeNumero.get(), matrizEsperada)

    def generarMatrizInicial(self):
        matriz = [
            [0,2,3],
            [4,0,5],
            [0,8,9],
        ]
        matrizEsperada = [
            [1,0,0],
            [0,1,0],
            [1,0,0],
        ]
        matrizGenerada = self.espaciosDeNumerosDisponibles.generarMatrizInicial(matriz)
        self.assertEqual(matrizGenerada , matrizEsperada)

    def guardarMatricesIniciales(self):
        matriz = [
            [1,0,0],
            [0,1,0],
            [1,0,0],
        ]
        self.espaciosDeNumerosDisponibles.guardarMatricesIniciales([1, 6, 7], matriz)
        matrices = self.espaciosDeNumerosDisponibles.get()
        matrizDeNumero: MatrizInterfaz = matrices[1]
        self.assertEqual(len(matrices), 3)
        self.assertIsInstance(matrizDeNumero, MatrizInterfaz)
        self.assertEqual(matrizDeNumero.get(), matriz)
            
    def get(self):
        pass
    
    def set(self):
        nuevosEspacios = self.espaciosDeNumerosDisponibles.get()
        nuevaMatrizDeNumero = [
            [1,0,0],
            [0,1,0],
            [1,0,0],
        ]
        nuevoNumero = Matriz()
        nuevoNumero.set(nuevaMatrizDeNumero)
        nuevosEspacios[9] = nuevoNumero
        self.espaciosDeNumerosDisponibles.set(nuevosEspacios)

        tamaño = len(self.espaciosDeNumerosDisponibles.get())
        self.assertEqual(tamaño, 4)
    
    def remove(self):
        self.espaciosDeNumerosDisponibles.remove(7)
        tamaño = len(self.espaciosDeNumerosDisponibles.get())
        self.assertEqual(tamaño, 3)
        self.assertFalse(self.espaciosDeNumerosDisponibles.contieneNumero(7))
    
    def contieneNumero(self):
        contieneNumero = self.espaciosDeNumerosDisponibles.contieneNumero(1)
        self.assertTrue(contieneNumero)
        contieneNumero = self.espaciosDeNumerosDisponibles.contieneNumero(2)
        self.assertFalse(contieneNumero)
        contieneNumero = self.espaciosDeNumerosDisponibles.contieneNumero(6)
        self.assertTrue(contieneNumero)
    
    def setConPosicion(self):
        self.espaciosDeNumerosDisponibles.setConPosicion(1, 2, 2, 1)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 2, 2)
        self.assertEqual(valor, 1)
    
    def getConPosicion(self):
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 0, 0)
        self.assertEqual(valor, 1)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 1, 1)
        self.assertEqual(valor, 1)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 2, 1)
        self.assertEqual(valor, 0)

    def limpiarFila(self):
        self.espaciosDeNumerosDisponibles.limpiarFila(1, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 0, 0)
        self.assertEqual(valor, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 0, 1)
        self.assertEqual(valor, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 0, 2)
        self.assertEqual(valor, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(1, 1, 1)
        self.assertEqual(valor, 1)


    def limpiarColumna(self):
        self.espaciosDeNumerosDisponibles.limpiarColumna(9, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(9, 0, 0)
        self.assertEqual(valor, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(9, 1, 0)
        self.assertEqual(valor, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(9, 2, 0)
        self.assertEqual(valor, 0)
        valor = self.espaciosDeNumerosDisponibles.getConPosicion(9, 1, 1)
        self.assertEqual(valor, 1)
        pass

    def getMatrizDeNumero(self):
        matrizDeNumero = self.espaciosDeNumerosDisponibles.getMatrizDeNumero(9)
        matrizEsperada = [
            [0,0,0],
            [0,1,0],
            [0,0,0],
        ]
        self.assertEqual(matrizDeNumero.get(), matrizEsperada)
        matrizDeNumero = self.espaciosDeNumerosDisponibles.getMatrizDeNumero(6)
        matrizEsperada = [
            [1,0,0],
            [0,1,0],
            [1,0,0],
        ]
        self.assertEqual(matrizDeNumero.get(), matrizEsperada)
        matrizDeNumero = self.espaciosDeNumerosDisponibles.getMatrizDeNumero(1)
        matrizEsperada = [
            [0,0,0],
            [0,1,0],
            [1,0,1],
        ]
        self.assertEqual(matrizDeNumero.get(), matrizEsperada)


if __name__ == '__main__':
    unittest.main()