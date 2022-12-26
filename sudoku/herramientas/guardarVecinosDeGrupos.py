from sudoku.interfaces.guardarVecinosDeGrupos import guardarVecinosDeGruposInterfaz

class guardarVecinosDeGrupos(guardarVecinosDeGruposInterfaz):
    def __init__(self) -> None:
        pass

    def guardar(self, grupos : list) -> list:
            grupos[1-1].guardarGruposVecinosEnFila([grupos[2-1],grupos[3-1]])
            grupos[1-1].guardarGruposVecinosEnColumna([grupos[4-1],grupos[7-1]])

            grupos[2-1].guardarGruposVecinosEnFila([grupos[1-1],grupos[3-1]])
            grupos[2-1].guardarGruposVecinosEnColumna([grupos[5-1],grupos[8-1]])

            grupos[3-1].guardarGruposVecinosEnFila([grupos[1-1],grupos[2-1]])
            grupos[3-1].guardarGruposVecinosEnColumna([grupos[6-1],grupos[9-1]])

            grupos[4-1].guardarGruposVecinosEnFila([grupos[5-1],grupos[6-1]])
            grupos[4-1].guardarGruposVecinosEnColumna([grupos[1-1],grupos[7-1]])

            grupos[5-1].guardarGruposVecinosEnFila([grupos[4-1],grupos[6-1]])
            grupos[5-1].guardarGruposVecinosEnColumna([grupos[2-1],grupos[8-1]])

            grupos[6-1].guardarGruposVecinosEnFila([grupos[4-1],grupos[5-1]])
            grupos[6-1].guardarGruposVecinosEnColumna([grupos[3-1],grupos[9-1]])

            grupos[7-1].guardarGruposVecinosEnFila([grupos[8-1],grupos[9-1]])
            grupos[7-1].guardarGruposVecinosEnColumna([grupos[1-1],grupos[4-1]])

            grupos[8-1].guardarGruposVecinosEnFila([grupos[7-1],grupos[9-1]])
            grupos[8-1].guardarGruposVecinosEnColumna([grupos[2-1],grupos[5-1]])

            grupos[9-1].guardarGruposVecinosEnFila([grupos[7-1],grupos[8-1]])
            grupos[9-1].guardarGruposVecinosEnColumna([grupos[3-1],grupos[6-1]])
            return grupos