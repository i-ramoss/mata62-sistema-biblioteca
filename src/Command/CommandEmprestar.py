from .ICommand import ICommand


class CommandEmprestar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade

        biblioteca = BibliotecaSingletonFacade()
        biblioteca.realizarEmprestimo(
            int(self.__restoComando[0]), int(self.__restoComando[1])
        )
