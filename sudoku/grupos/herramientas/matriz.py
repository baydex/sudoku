class Matriz:
    def __init__(self) -> None:
        self.matriz = list()

    def get(self):
        return self.matriz

    def set(self, value):
        self.matriz = value
    
    def getConPosicion(self, x: int, y: int):
        return self.matriz[x][y]
    
    def setConPosicion(self, x: int, y: int, value: int):
        self.matriz[x][y] = value
