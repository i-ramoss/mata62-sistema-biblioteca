from .Usuario import Usuario
from ..EmprestimoBehavior import IEmprestimoBehavior
from ..Listener import IListener

class Professor(Usuario,IListener):
    def __init__(self, codigo:int, nome:str, emprestimoBehavior:IEmprestimoBehavior):
        super().__init__(codigo, nome, emprestimoBehavior)
        self.__vezesNotificado = 0
    
    def update(self):
        self.__vezesNotificado += 1
        pass

    def getVezesNotificado(self):
        return self.__vezesNotificado
