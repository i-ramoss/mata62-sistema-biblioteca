from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede

class CommandNotificacaoProfessor(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.mostraNotificaProfessor(self.__restoComando[0], self.__restoComando[1])
