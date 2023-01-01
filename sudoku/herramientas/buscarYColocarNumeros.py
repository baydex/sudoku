from copy import deepcopy

from sudoku.interfaces.buscarYColocarNumeros import buscarYColocarNumeros
from sudoku.grupos.interfaces.grupos import Grupo

class buscarYColocarNumerosImp(buscarYColocarNumeros):  
    def __init__(self,grupos) -> None:
        self.__grupos = grupos

    def ejecutar(self) -> list:
        self.antiguosEspaciosDeNumerosDisponibles = list()
        self.guardarNumerosDisponibles()
        self.repetirBusqueda()
        return self.__grupos

    def guardarNumerosDisponibles(self) -> None:
        self.nuevosEspaciosDeNumerosDisponibles = list()
        for grupo in self.__grupos:
            grupo: Grupo
            self.nuevosEspaciosDeNumerosDisponibles.append(grupo.espaciosDeNumerosDisponibles.get())

    def repetirBusqueda(self) -> None:
        self.huboProgreso = True   

        while self.huboProgreso:
            self.progresarEnBuqueda()
            self.verificarProgresoEnBusqueda()

    def progresarEnBuqueda(self) -> None:
        for grupo in self.__grupos:
            grupo: Grupo
            grupo.buscarNumeros()
            # grupo.colocarNumeros()

    def verificarProgresoEnBusqueda(self) -> None:
        if self.nuevosEspaciosDeNumerosDisponibles == self.antiguosEspaciosDeNumerosDisponibles:
            self.huboProgreso = False
        else:
            self.antiguosEspaciosDeNumerosDisponibles = deepcopy(self.nuevosEspaciosDeNumerosDisponibles)
            self.guardarNumerosDisponibles()