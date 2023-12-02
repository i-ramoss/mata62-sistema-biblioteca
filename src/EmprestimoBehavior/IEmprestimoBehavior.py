from abc import ABC, abstractmethod


class IEmprestimoBehavior(ABC):
    @abstractmethod
    def verificarPossibilidadeDeEmprestimo(
        self, codigoUsuario: int, codigoLivro: int
    ) -> bool:
        raise NotImplementedError

    def getIntervaloDeTempoDeEmprestimo(self) -> int:
        raise NotImplementedError
