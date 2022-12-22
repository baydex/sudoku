
import os
from sudoku.sudok import Sudoku

# {
#     "0": [0,0,4,  7,1,0,  0,0,0],
#     "1": [0,7,2,  8,0,6,  5,0,0],
#     "2": [0,0,0,  0,0,5,  0,0,7],

#     "3": [0,1,0,  6,9,0,  2,0,0],
#     "4": [3,9,0,  0,5,0,  0,0,0],
#     "5": [0,0,0,  0,0,0,  0,8,5],

#     "6": [0,0,1,  2,3,0,  8,0,4],
#     "7": [0,0,3,  5,0,4,  0,0,2],
#     "8": [2,4,0,  9,0,0,  0,0,0]

# nojada }

os.system("cls")
sudoku = Sudoku()

sudoku.cargarSudoku("data.json")

sudoku.resolver()

sudoku.show()

# sudoku.grupos[0].verEspaciosDeNumerosDisponibles()
