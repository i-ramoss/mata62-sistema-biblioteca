from .ICommand import ICommand


class CommandNotificacaoProfessor(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade

        biblioteca = BibliotecaSingletonFacade()
        biblioteca.mostraNotificaoProfessor(int(self.__restoComando[0]))
