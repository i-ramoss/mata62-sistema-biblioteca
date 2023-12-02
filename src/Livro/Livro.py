from .Exemplar import Exemplar
from ..Enums import StatusExemplar


class Livro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        editora: str,
        autores: list[str],
        edicao: str,
        anoPublicacao: int,
    ) -> None:
        self.__codigo = codigo
        self.__titulo = titulo
        self.__editora = editora
        self.__autores = autores
        self.__edicao = edicao
        self.__anoPublicacao = anoPublicacao
        self.__qtdDisponivel = 0
        self.__exemplares: list[Exemplar] = [Exemplar(1)]

    def getCodigo(self) -> int:
        return self.__codigo

    def getTitulo(self) -> str:
        return self.__titulo

    def getQtdDisponivel(self) -> int:
        exemplaresDisponiveis = 0

        for exemplar in self.__exemplares:
            if exemplar.getStatus() == StatusExemplar.DISPONIVEL:
                exemplaresDisponiveis += 1

        return exemplaresDisponiveis

    def setQtdDisponivel(self, qtdDisponivel: int) -> None:
        self.__qtdDisponivel += qtdDisponivel

    def listarExemplares(self) -> list[Exemplar]:
        return self.__exemplares

    def buscarExemplaresPeloStatus(self, status: str) -> list[Exemplar]:
        exemplares = []

        for exemplar in self.__exemplares:
            if exemplar.getStatus() == status:
                exemplares.append(exemplar)

        return exemplares

    def buscarExemplarPeloCodigo(self, codigoExemplar: int) -> Exemplar:
        for exemplar in self.__exemplares:
            if exemplar.getCodigo() == codigoExemplar:
                return exemplar

    def __criarExemplar(self) -> None:
        ultimoCodigo = self.__exemplares[-1].getCodigo()

        self.__exemplares.append(Exemplar(ultimoCodigo + 1))

    def criarExemplares(self, qtdExemplares: int) -> None:
        for _ in range(qtdExemplares):
            self.__criarExemplar()

    def getCodigoProximoExemplarASerEmprestado(self) -> int:
        for exemplar in self.__exemplares:
            if exemplar.getStatus() == StatusExemplar.DISPONIVEL:
                exemplar.setStatus(StatusExemplar.EMPRESTADO)
                return exemplar.getCodigo()
