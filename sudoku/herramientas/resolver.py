from sudoku.herramientas.configurarGrupos import ConfigurarGrupos
from sudoku.herramientas.buscarYColocarNumeros import buscarYColocarNumeros
from sudoku.interfaces.resolver import ResolverInterfaz

class Resolver(ResolverInterfaz):
    def __init__(self) -> None:
        self.__grupos = list()

    def resolver(self, grupos: list) -> list:
        self.__grupos = grupos
        self.configurarGrupos()
        self.buscarYColocarNumeros()
        self.sudoku = self.__grupos
        return self.sudoku

    def configurarGrupos(self) -> None:
        self.__grupos = ConfigurarGrupos(self.__grupos).configurar()

    def buscarYColocarNumeros(self) -> None:
        self.__grupos = buscarYColocarNumeros(self.__grupos).ejecutar()