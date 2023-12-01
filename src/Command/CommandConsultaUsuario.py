from .ICommand import ICommand
from ..Biblioteca import Biblioteca

class CommandConsultaUsuario(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(self): 
        biblioteca = Biblioteca()
        biblioteca.ConsultaUsuario(self.__restoComando[0])
