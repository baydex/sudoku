from sudoku.interfaces.show import ShowInterfaz
from sudoku.grupos.interfaces.grupos import GrupoInterfaz

class Show(ShowInterfaz):

    def __init__(self) -> None:
        self.sudoku = list()

    def show(self, sudoku: list):
        self.sudoku = sudoku
        for i in range(0,9,3):
            for j in range(3):
                for k in range(3):
                    print(self.sudoku[i+k].matriz.get()[j],end=" ")
                print()
            print()