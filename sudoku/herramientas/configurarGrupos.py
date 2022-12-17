from sudoku.herramientas.guardarVecinosDeGrupos import guardarVecinosDeGrupos
from sudoku.grupos.grupos import Grupo
class ConfigurarGrupos:    
    def __init__(self, grupos: list) -> None:
        self.grupos = grupos

    def configurar(self) -> list:
        self._separarSudokuEnGrupos()
        self.guardarVecinosDeGrupos()
        self.limpiarNumerosDisponiblesDeGrupos()
        return self.grupos

    def _separarSudokuEnGrupos(self) -> None:
        grupos = list()
        for j in range(0,7,3):
            for i in range(0,7,3):
                matrizDeGrupo = []
                for k in range(3):
                    matrizDeGrupo.append(self.grupos[str(j+k)][i:i+3])
                print(matrizDeGrupo)
                grupo = Grupo()
                grupo.guardarMatriz(matrizDeGrupo)
                grupos.append(grupo)

        self.grupos = grupos

    def guardarVecinosDeGrupos(self) -> None:
        self.grupos = guardarVecinosDeGrupos().guardar(self.grupos)
    
    def limpiarNumerosDisponiblesDeGrupos(self) -> None:
        for grupo in self.grupos: 
            grupo:Grupo
            grupo.limpiarNumerosDisponibles()
