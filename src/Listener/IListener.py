from abc import ABC, abstractmethod

class IListener(ABC):
    _restoComando: str
    @abstractmethod
    def update(self):
        raise NotImplementedError
