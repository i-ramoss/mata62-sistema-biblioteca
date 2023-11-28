from abc import ABC, abstractmethod


class IRegraEmprestimo(ABC):
    @abstractmethod
    def realizar_emprestiomo(self):
        raise NotImplementedError
