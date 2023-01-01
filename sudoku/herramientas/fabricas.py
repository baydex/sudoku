from sudoku.herramientas.cargarSudoku import cargarSudokuImp, cargarSudoku
from sudoku.herramientas.resolver import ResolverImp, Resolver
from sudoku.herramientas.show import ShowImp, Show

def cargarSudokuFact() -> cargarSudoku:
    return cargarSudokuImp()

def resolverFact() -> Resolver:
    return ResolverImp()

def showFact() -> Show:
    return ShowImp()

