from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacade


class CommandObservar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        biblioteca = BibliotecaSingletonFacade()
        biblioteca.observarLivroProfessor(
            self.__restoComando[0], self.__restoComando[1]
        )
