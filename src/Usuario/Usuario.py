from ..EmprestimoBehavior import IEmprestimoBehavior


class Usuario:
    def __init__(
        self, codigo: int, nome: str, emprestimoBehavior: IEmprestimoBehavior
    ) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__emprestimoBehavior = emprestimoBehavior

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getEmprestimoBehavior(self):
        self.__emprestimoBehavior.verificarPossibilidadeDeEmprestimo()
