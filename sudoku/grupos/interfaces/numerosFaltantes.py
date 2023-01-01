from abc import abstractmethod
from abc import ABCMeta

class NumerosFaltantes(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.__numerosFaltantes: list

    @abstractmethod
    def crear(self, matriz: list) -> None:
        pass

    @abstractmethod
    def get(self) -> list:
        pass

    @abstractmethod
    def set(self, value: list) -> None:
        pass

    @abstractmethod
    def remove(self, value: int) -> None:
        pass