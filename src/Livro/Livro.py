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
        self.__qtdReservas = 0

    def getCodigo(self) -> int:
        return self.__codigo

    def getTitulo(self) -> str:
        return self.__titulo

    def getQtdDisponivel(self) -> int:
        return self.__qtdDisponivel

    def setQtdDisponivel(self, qtdDisponivel: int) -> None:
        self.__qtdDisponivel += qtdDisponivel

    def getQtdReservas(self) -> int:
        return self.__qtdReservas

    def adicionarReserva(self) -> None:
        self.__qtdReservas += 1

    def removerReserva(self) -> None:
        self.__qtdReservas -= 1
