from abc import abstractmethod
from abc import ABCMeta

class guardarVecinosDeGruposInterfaz(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def guardar(self, grupos : list) -> list:
            pass