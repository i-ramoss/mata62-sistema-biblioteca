from .ICommand import ICommand


class CommandAddLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade
        biblioteca = BibliotecaSingletonFacade()
        biblioteca.adicionarLivro(self.__restoComando[0])
