from sudoku.herramientas.configurarGrupos import ConfigurarGrupos
from sudoku.herramientas.buscarYColocarNumeros import buscarYColocarNumeros

class Resolver:
    def __init__(self) -> None:
        self.grupos = list()

    def resolver(self, grupos) -> list:
        self.grupos = grupos
        self.configurarGrupos()
        self.buscarYColocarNumeros()
        self.sudoku = self.grupos
        return self.sudoku

    def configurarGrupos(self) -> None:
        self.grupos = ConfigurarGrupos(self.grupos).configurar()

    def buscarYColocarNumeros(self) -> None:
        self.grupos = buscarYColocarNumeros(self.grupos).ejecutar()