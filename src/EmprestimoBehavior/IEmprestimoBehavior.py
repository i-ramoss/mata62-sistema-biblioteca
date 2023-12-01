from abc import ABC, abstractmethod


class IEmprestimoBehavior(ABC):
    @abstractmethod
    def verificarPossibilidadeDeEmprestimo(self) -> bool:
        raise NotImplementedError

    def getIntervaloDeTempoDeEmprestimo(self) -> int:
        raise NotImplementedError
