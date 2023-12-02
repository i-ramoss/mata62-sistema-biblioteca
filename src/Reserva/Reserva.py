from datetime import datetime

from ..Usuario import Usuario
from ..Livro import Livro


class Reserva:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.__usuario = usuario
        self.__livro = livro
        self.__dataSolicitacao = datetime.now()

    def getUsuario(self) -> Usuario:
        return self.__usuario

    def getLivro(self) -> Livro:
        return self.__livro

    def getDataSolicitacao(self) -> datetime:
        return self.__dataSolicitacao.strftime("%d/%m/%Y")
