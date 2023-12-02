from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacade


class CommandNotificacaoProfessor(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        biblioteca = BibliotecaSingletonFacade()
        biblioteca.mostraNotificaoProfessor(self.__restoComando[0])
