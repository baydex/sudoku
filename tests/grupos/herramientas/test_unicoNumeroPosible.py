import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.herramientas.unicoNumeroPosible import UnicoNumeroPosible
from sudoku.grupos.herramientas.espaciosDeNumerosDisponibles import EspaciosDeNumerosDisponibles
from sudoku.grupos.herramientas.numerosFaltantes import NumerosFaltantes
from sudoku.grupos.herramientas.vecinos import Vecinos
from sudoku.grupos.grupos import Grupo

class Test_UnicoNumeroPosible(unittest.TestCase):

    def test_unicoNumeroPosible(self):
        
        self.unicoNumeroPosible = UnicoNumeroPosible()
        
        self.enGrupo()
        self.enCasilla()
        self.enFila()
        self.enColumna()
        self.get()
        self.restaurar()

    def enGrupo(self):
        self.unicoNumeroPosible = UnicoNumeroPosible()
        espaciosDeNumerosDisponibles = EspaciosDeNumerosDisponibles()
        numerosFaltantes = NumerosFaltantes()

        matriz = [
            [0,0,1],
            [0,0,0],
            [0,0,0]
        ]

        numerosFaltantes.crear(matriz)
        espaciosDeNumerosDisponibles.crear(numerosFaltantes.get() ,matriz)

        self.unicoNumeroPosible.enGrupo(espaciosDeNumerosDisponibles, 2)
        self.assertFalse(self.unicoNumeroPosible.get())

        espaciosDeNumerosDisponibles.limpiarFila(2, 0)
        espaciosDeNumerosDisponibles.limpiarFila(2, 1)
        espaciosDeNumerosDisponibles.limpiarColumna(2, 0)
        espaciosDeNumerosDisponibles.limpiarColumna(2, 1)

        self.unicoNumeroPosible.enGrupo(espaciosDeNumerosDisponibles, 2)
        self.assertIsInstance(self.unicoNumeroPosible.get(), list)

        self.unicoNumeroPosible = UnicoNumeroPosible()
        espaciosDeNumerosDisponibles.limpiarFila(2, 2)
        self.unicoNumeroPosible.enGrupo(espaciosDeNumerosDisponibles, 2)
        self.assertFalse(self.unicoNumeroPosible.get())

    def enCasilla(self):
        self.unicoNumeroPosible = UnicoNumeroPosible()
        espaciosDeNumerosDisponibles = EspaciosDeNumerosDisponibles()
        numerosFaltantes = NumerosFaltantes()

        matriz = [
            [1,2,3],
            [4,5,6],
            [0,0,0]
        ]

        numerosFaltantes.crear(matriz)
        espaciosDeNumerosDisponibles.crear(numerosFaltantes.get() ,matriz)

        self.unicoNumeroPosible.enCasilla(espaciosDeNumerosDisponibles, 7)
        self.assertFalse(self.unicoNumeroPosible.get())

        espaciosDeNumerosDisponibles.limpiarColumna(8, 0)
        espaciosDeNumerosDisponibles.limpiarColumna(9, 0)

        self.unicoNumeroPosible.enCasilla(espaciosDeNumerosDisponibles, 7)
        self.assertIsInstance(self.unicoNumeroPosible.get(), list)

        self.unicoNumeroPosible = UnicoNumeroPosible()
        espaciosDeNumerosDisponibles.limpiarFila(7, 2)
        self.unicoNumeroPosible.enCasilla(espaciosDeNumerosDisponibles, 7)
        self.assertFalse(self.unicoNumeroPosible.get())

    def enFila(self):
        matriz = [
            [1,2,3],
            [4,5,6],
            [0,0,0],
        ]
        matrizVecino1 = [
            [1,2,3],
            [0,0,0],
            [4,5,6],
        ]
        matrizVecino2 = [
            [0,0,0],
            [1,2,3],
            [4,5,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, False)

        self.afirmacionFilaColumna(espaciosDeNumerosDisponibles, vecinos, False)
        # ///////////////////////////////////////////////////
        
        matriz = [
            [1,2,3],
            [4,5,6],
            [8,9,0],
        ]

        matrizVecino1 = [
            [1,2,3],
            [0,0,0],
            [4,5,6],
        ]
        matrizVecino2 = [
            [0,0,0],
            [1,2,3],
            [4,5,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, False)

        self.afirmacionFilaColumna(espaciosDeNumerosDisponibles, vecinos, False)
        # ///////////////////////////////////////////////////
        
        matriz = [
            [1,2,3],
            [4,5,6],
            [0,0,0],
        ]

        matrizVecino1 = [
            [1,2,3],
            [0,0,0],
            [4,5,6],
        ]
        matrizVecino2 = [
            [0,0,0],
            [1,2,3],
            [4,5,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, False)

        self.unicoNumeroPosible.enFila(espaciosDeNumerosDisponibles, 7, vecinos)

        self.assertFalse(self.unicoNumeroPosible.get())
        # ///////////////////////////////////////////////////
        
        matriz = [
            [1,2,3],
            [4,5,6],
            [0,0,0],
        ]

        matrizVecino1 = [
            [1,2,3],
            [4,5,6],
            [0,0,0],
        ]
        matrizVecino2 = [
            [0,0,0],
            [1,2,3],
            [4,5,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, False)

        espaciosDeNumerosDisponibles.limpiarColumna(7,0)
        espaciosDeNumerosDisponibles.limpiarColumna(7,1)

        self.unicoNumeroPosible.enFila(espaciosDeNumerosDisponibles, 7, vecinos)

        self.assertFalse(self.unicoNumeroPosible.get())
        # ///////////////////////////////////////////////////
                
        matriz = [
            [1,2,3],
            [4,5,6],
            [0,0,0],
        ]

        matrizVecino1 = [
            [1,2,3],
            [4,5,6],
            [0,0,0],
        ]
        matrizVecino2 = [
            [0,0,0],
            [1,2,3],
            [4,5,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, False)

        vecinos.getFila()[0].espaciosDeNumerosDisponibles.limpiarColumna(7, 0)
        vecinos.getFila()[0].espaciosDeNumerosDisponibles.limpiarColumna(7, 1)
        vecinos.getFila()[0].espaciosDeNumerosDisponibles.limpiarColumna(7, 2)

        self.afirmacionFilaColumna(espaciosDeNumerosDisponibles, vecinos, False)
    
    def configurarFilaColumna(self, matriz: list, matrizVecino1: list, matrizVecino2: list, esColumna: bool):
        self.unicoNumeroPosible.restaurar()
        espaciosDeNumerosDisponibles = EspaciosDeNumerosDisponibles()
        numerosFaltantes = NumerosFaltantes()
        vecinos = Vecinos()
        vecino1 = Grupo()
        vecino2 = Grupo()


        numerosFaltantes.crear(matriz)
        espaciosDeNumerosDisponibles.crear(numerosFaltantes.get() ,matriz)


        vecino1.guardarMatriz(matrizVecino1)
        vecino2.guardarMatriz(matrizVecino2)

        if esColumna:
            vecinos.setColumna([vecino1, vecino2])
        else:
            vecinos.setFila([vecino1, vecino2])
        return espaciosDeNumerosDisponibles, vecinos

    def afirmacionFilaColumna(self, espaciosDeNumerosDisponibles: EspaciosDeNumerosDisponibles, vecinos: Vecinos, esColumna: bool):
        if esColumna:
            espaciosDeNumerosDisponibles.limpiarFila(7,0)
            espaciosDeNumerosDisponibles.limpiarFila(7,1)

            self.unicoNumeroPosible.enColumna(espaciosDeNumerosDisponibles, 7, vecinos)
        else:
            espaciosDeNumerosDisponibles.limpiarColumna(7,0)
            espaciosDeNumerosDisponibles.limpiarColumna(7,1)

            self.unicoNumeroPosible.enFila(espaciosDeNumerosDisponibles, 7, vecinos)

        self.assertIsInstance(self.unicoNumeroPosible.get(), list)


    def enColumna(self):
        matriz = [
            [1,4,0],
            [2,5,0],
            [3,6,0],
        ]

        matrizVecino1 = [
            [1,0,4],
            [2,0,5],
            [3,0,6],
        ]
        matrizVecino2 = [
            [0,1,4],
            [0,2,5],
            [0,3,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, True)

        self.afirmacionFilaColumna(espaciosDeNumerosDisponibles, vecinos, True)
        # ///////////////////////////////////////////////////
        
        matriz = [
            [1,4,8],
            [2,5,9],
            [3,6,0],
        ]

        matrizVecino1 = [
            [1,0,4],
            [2,0,5],
            [3,0,6],
        ]
        matrizVecino2 = [
            [0,1,4],
            [0,2,5],
            [0,3,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, True)

        self.afirmacionFilaColumna(espaciosDeNumerosDisponibles, vecinos, True)
        # ///////////////////////////////////////////////////

        matriz = [
            [1,4,0],
            [2,5,0],
            [3,6,0],
        ]

        matrizVecino1 = [
            [1,0,4],
            [2,0,5],
            [3,0,6],
        ]
        matrizVecino2 = [
            [0,1,4],
            [0,2,5],
            [0,3,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, True)

        self.unicoNumeroPosible.enColumna(espaciosDeNumerosDisponibles, 7, vecinos)

        self.assertFalse(self.unicoNumeroPosible.get())
        # ///////////////////////////////////////////////////
        
        matriz = [
            [1,4,0],
            [2,5,0],
            [3,6,0],
        ]

        matrizVecino1 = [
            [1,4,0],
            [2,5,0],
            [3,6,0],
        ]
        matrizVecino2 = [
            [0,1,4],
            [0,2,5],
            [0,3,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, True)
        
        espaciosDeNumerosDisponibles.limpiarFila(7,0)
        espaciosDeNumerosDisponibles.limpiarFila(7,1)

        self.unicoNumeroPosible.enColumna(espaciosDeNumerosDisponibles, 7, vecinos)

        self.assertFalse(self.unicoNumeroPosible.get())
        # ///////////////////////////////////////////////////
        
        matriz = [
            [1,4,0],
            [2,5,0],
            [3,6,0],
        ]

        matrizVecino1 = [
            [1,4,0],
            [2,5,0],
            [3,6,0],
        ]
        matrizVecino2 = [
            [0,1,4],
            [0,2,5],
            [0,3,6],
        ]

        espaciosDeNumerosDisponibles, vecinos = self.configurarFilaColumna(matriz, matrizVecino1, matrizVecino2, True)


        vecinos.getColumna()[0].espaciosDeNumerosDisponibles.limpiarFila(7, 0)
        vecinos.getColumna()[0].espaciosDeNumerosDisponibles.limpiarFila(7, 1)
        vecinos.getColumna()[0].espaciosDeNumerosDisponibles.limpiarFila(7, 2)

        self.afirmacionFilaColumna(espaciosDeNumerosDisponibles, vecinos, True)
    
    def get(self):
        self.assertIsInstance(self.unicoNumeroPosible.get(), list)
        self.unicoNumeroPosible.restaurar()
        self.assertIsInstance(self.unicoNumeroPosible.get(), bool)

    def restaurar(self):
        self.unicoNumeroPosible.restaurar()
        self.assertFalse(self.unicoNumeroPosible.get())
    