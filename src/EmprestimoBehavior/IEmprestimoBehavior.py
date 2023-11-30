from abc import ABC, abstractmethod


class IEmprestimoBehavior(ABC):
    @abstractmethod
    def verificarPossibilidadeDeEmprestimo(self):
        raise NotImplementedError
