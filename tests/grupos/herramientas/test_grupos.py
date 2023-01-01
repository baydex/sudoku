import unittest

import sys
sys.path.append("../../../")

from sudoku.grupos.grupos import GrupoImp


class Test_Grupos(unittest.TestCase):
    
    def test_grupos(self):
        self.grupo = GrupoImp()
        self.guardarMatriz()
        self.limpiarNumerosDisponiblesEnVecinos()
        self.buscarNumeros()
        self.verificarNumero()
        self.ponerNumeroEnMatriz()
        self.eliminarDeNumerosFaltantes()
        self.eliminarMatrizDeNumeroFaltante()
        self.esUnicoNumeroPosibleEnGrupo()
        self.esUnicoNumeroPosibleEnCasilla()
        self.esUnicoNumeroPosibleEnFila()
        self.esUnicoNumeroPosibleEnColumna()
        self.ponerNumero()

    def guardarMatriz(self):
        pass

    def limpiarNumerosDisponiblesEnVecinos(self):
        pass

    def buscarNumeros(self):
        pass

    def verificarNumero(self):
        pass

    def ponerNumeroEnMatriz(self):
        pass

    def eliminarDeNumerosFaltantes(self):
        pass

    def eliminarMatrizDeNumeroFaltante(self):
        pass

    def esUnicoNumeroPosibleEnGrupo(self):    
        pass

    def esUnicoNumeroPosibleEnCasilla(self):
        pass

    def esUnicoNumeroPosibleEnFila(self):
        pass

    def esUnicoNumeroPosibleEnColumna(self):
        pass
        
    def ponerNumero(self):
        pass

