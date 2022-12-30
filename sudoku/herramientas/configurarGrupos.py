from sudoku.herramientas.guardarVecinosDeGrupos import guardarVecinosDeGrupos
from sudoku.grupos.grupos import Grupo
from sudoku.interfaces.configurarGrupos import ConfigurarGruposInterfaz


class ConfigurarGrupos(ConfigurarGruposInterfaz): 
       
    def __init__(self, grupos: list) -> None:
        self.__grupos = grupos

    def configurar(self) -> list:
        self.separarSudokuEnGrupos()
        self.guardarVecinosDeGrupos()
        self.limpiarNumerosDisponiblesDeGrupos()
        return self.__grupos

    def separarSudokuEnGrupos(self) -> None:
        grupos = list()
        for j in range(0,7,3):
            for i in range(0,7,3):
                matrizDeGrupo = []
                for k in range(3):
                    matrizDeGrupo.append(self.__grupos[str(j+k)][i:i+3])
                grupo = Grupo()
                grupo.guardarMatriz(matrizDeGrupo)
                grupos.append(grupo)

        self.__grupos = grupos

    def guardarVecinosDeGrupos(self) -> None:
        self.__grupos = guardarVecinosDeGrupos().guardar(self.__grupos)
    
    def limpiarNumerosDisponiblesDeGrupos(self) -> None:

        for grupo in self.__grupos: 
            grupo:Grupo            
            grupo.limpiarNumerosDisponiblesEnVecinos()
