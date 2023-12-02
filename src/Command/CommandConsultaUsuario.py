from .ICommand import ICommand

class CommandConsultaUsuario(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(self): 
        from ..Biblioteca import Biblioteca
        biblioteca = Biblioteca()
        biblioteca.ConsultaUsuario(self.__restoComando[0])
