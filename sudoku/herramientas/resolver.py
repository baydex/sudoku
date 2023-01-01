from sudoku.herramientas.buscarYColocarNumeros import buscarYColocarNumerosImp
from sudoku.herramientas.configurarGrupos import ConfigurarGruposImp
from sudoku.interfaces.resolver import Resolver

class ResolverImp(Resolver):
    def __init__(self) -> None:
        self.__grupos = list()

    def resolver(self, grupos: list) -> list:
        self.__grupos = grupos
        self.configurarGrupos()
        self.buscarYColocarNumeros()
        self.sudoku = self.__grupos
        return self.sudoku

    def configurarGrupos(self) -> None:
        self.__grupos = ConfigurarGruposImp(self.__grupos).configurar()

    def buscarYColocarNumeros(self) -> None:
        self.__grupos = buscarYColocarNumerosImp(self.__grupos).ejecutar()