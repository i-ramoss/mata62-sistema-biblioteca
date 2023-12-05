from .Usuario import Usuario
from ..EmprestimoBehavior import EmprestimoProfessor
from ..Listener import IListener


class Professor(Usuario, IListener):
    def __init__(self, codigo: int, nome: str) -> None:
        super().__init__(codigo, nome, EmprestimoProfessor())
        self.__vezesNotificado: int = 0

    def update(self) -> None:
        self.__vezesNotificado += 1

    def getVezesNotificado(self) -> int:
        return self.__vezesNotificado
