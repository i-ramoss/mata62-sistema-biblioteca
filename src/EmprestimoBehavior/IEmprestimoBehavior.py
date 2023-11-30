from abc import ABC, abstractmethod


class IRegraEmprestimo(ABC):
    @abstractmethod
    def realizarEmprestiomo(self):
        raise NotImplementedError
