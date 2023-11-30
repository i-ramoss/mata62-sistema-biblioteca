from abc import ABC, abstractmethod

class ICommand(ABC):
    _restoComando: str
    @abstractmethod
    def execute(self):
        raise NotImplementedError
