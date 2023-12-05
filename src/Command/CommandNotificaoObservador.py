from .ICommand import ICommand


class CommandNotificacaoObservador(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade
        from ..Console import ConsoleSingleton
        try:
            biblioteca = BibliotecaSingletonFacade()
            biblioteca.mostrarNotificacaoObservador(int(self.__restoComando[0]))
        except IndexError:
            console = ConsoleSingleton()
            console.print("Houve um erro no formato do seu comando")

