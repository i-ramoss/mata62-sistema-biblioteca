from ..EmprestimoBehavior import IEmprestimoBehavior


class Usuario:
    def __init__(
        self, codigo: int, nome: str, emprestimoBehavior: IEmprestimoBehavior
    ) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__emprestimoBehavior = emprestimoBehavior

    def getCodigo(self) -> int:
        return self.__codigo

    def getNome(self) -> str:
        return self.__nome

    def getEmprestimoBehavior(self) -> IEmprestimoBehavior:
        return self.__emprestimoBehavior

    def getIntervaloDeTempoDeEmprestimo(self) -> int:
        return self.__emprestimoBehavior.getIntervaloDeTempoDeEmprestimo()

    def verificarPossibilidadeDeEmprestimo(
        self, codigoUsuario: int, codigoLivro: int
    ) -> bool:
        return self.__emprestimoBehavior.verificarPossibilidadeDeEmprestimo(
            codigoUsuario, codigoLivro
        )
