from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede

class CommandNotificacaoProfessor(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(self): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.mostraNotificaoProfessor(self.__restoComando[0])
