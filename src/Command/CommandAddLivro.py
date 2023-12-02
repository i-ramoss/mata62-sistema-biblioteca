from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacade


class CommandAddLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        biblioteca = BibliotecaSingletonFacade()
        biblioteca.adicionarLivro(self.__restoComando[0])
