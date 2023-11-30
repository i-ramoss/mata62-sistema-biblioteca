from ..EmprestimoBehavior import IEmprestimoBehavior


class Usuario:
    def __init__(
        self, codigo: int, nome: str, emprestimoBehavior: IEmprestimoBehavior
    ) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__emprestimoBehavior = emprestimoBehavior
        self.__qtdReservas = 0

    def getCodigo(self) -> int:
        return self.__codigo

    def getNome(self) -> str:
        return self.__nome

    def getEmprestimoBehavior(self) -> IEmprestimoBehavior:
        self.__emprestimoBehavior.verificarPossibilidadeDeEmprestimo()

    def getQtdReservas(self) -> int:
        return self.__qtdReservas

    def adicionarReserva(self) -> None:
        self.__qtdReservas += 1

    def removerReserva(self) -> None:
        self.__qtdReservas -= 1
