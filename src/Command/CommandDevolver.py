from .ICommand import ICommand


class CommandDevolver(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade

        biblioteca = BibliotecaSingletonFacade()
        biblioteca.realizarDevolucao(
            int(self.__restoComando[0]), int(self.__restoComando[1])
        )
