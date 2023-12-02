from datetime import datetime, timedelta

from ..Usuario import Usuario
from ..Livro import Livro
from ..Enums import StatusEmprestimo, StatusExemplar


class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.__usuario = usuario
        self.__livro = livro
        self.__codigoExemplar = self.__livro.getCodigoProximoExemplarASerEmprestado()
        self.__data_inicio = datetime.now()
        self.__data_devolucao = self.__data_inicio + timedelta(
            days=usuario.getIntervaloDeTempoDeEmprestimo()
        )
        self.__status = StatusEmprestimo.EM_ANDAMENTO

    def getUsuario(self) -> Usuario:
        return self.__usuario

    def getLivro(self) -> Livro:
        return self.__livro

    def getCodigoExemplar(self) -> int:
        return self.__codigoExemplar

    def getDataInicio(self) -> datetime:
        return self.__data_inicio.strftime("%d/%m/%Y")

    def getDataDevolucao(self) -> datetime:
        return self.__data_devolucao.strftime("%d/%m/%Y")

    def getStatus(self) -> StatusEmprestimo:
        return self.__status

    def finalizar(self) -> None:
        exemplar = self.__livro.buscarExemplarPeloCodigo(self.__codigoExemplar)

        self.__data_devolucao = datetime.now()
        self.__status = StatusEmprestimo.FINALIZADO
        exemplar.setStatus(StatusExemplar.DISPONIVEL)
