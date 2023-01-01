import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.herramientas.numerosFaltantes import NumerosFaltantesImp
from sudoku.grupos.herramientas.matriz import MatrizImp

class Test_NumerosFaltantes(unittest.TestCase):
    
    def test_numerosFaltantes(self):
        self.numerosFaltantes = NumerosFaltantesImp()
        self.crear()
        self.get()
        self.set()
        self.remove()

    def crear(self):
        matriz = MatrizImp()
        matriz = [
                    [0, 0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0]
                    ]
        esperado = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.verificarMatrizCreada(matriz, esperado)
        
        matriz= [
                    [1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]
                    ]
        esperado = list()

        self.verificarMatrizCreada(matriz, esperado)
        
        matriz = [
                        [1, 0, 0], 
                        [8, 5, 0], 
                        [0, 0, 3]
                    ]
        esperado = [2, 4, 6, 7, 9]
        self.verificarMatrizCreada(matriz, esperado)

    def verificarMatrizCreada(self, matriz: list, esperado: list):
        self.numerosFaltantes.crear(matriz)
        matrizComparativa = esperado
        self.assertEqual(self.numerosFaltantes.get(), matrizComparativa)

    def get(self):
        numeros = self.numerosFaltantes.get()
        esperado = [2, 4, 6, 7, 9]
        self.assertEqual(numeros, esperado)

    def set(self):
        self.numerosFaltantes.set([1,2,3])
        esperado = [1, 2, 3]
        numeros = self.numerosFaltantes.get()
        self.assertEqual(numeros, esperado)

    def remove(self):
        self.numerosFaltantes.remove(2)
        esperado = [1, 3]
        numeros = self.numerosFaltantes.get()
        self.assertEqual(numeros, esperado)