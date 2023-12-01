from datetime import datetime, timedelta

from ..Usuario import Usuario
from ..Livro import Livro
from ..Enums import Status


class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.__usuario = usuario
        self.__livro = livro
        self.__data_inicio = datetime.now()
        self.__data_devolucao = self.__data_inicio + timedelta(
            days=usuario.getIntervaloDeTempoDeEmprestimo()
        )
        self.__status = Status.EM_ANDAMENTO

    def getStatus(self) -> Status:
        return self.__status

    def getUsuario(self) -> Usuario:
        return self.__usuario
