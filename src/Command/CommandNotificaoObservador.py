from .ICommand import ICommand


class CommandNotificacaoObservador(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade

        biblioteca = BibliotecaSingletonFacade()
        biblioteca.mostrarNotificacaoObservador(int(self.__restoComando[0]))
