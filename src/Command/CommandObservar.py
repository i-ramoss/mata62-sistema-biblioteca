from .ICommand import ICommand


class CommandObservar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade
        from ..Console import ConsoleSingleton
        try:
            biblioteca = BibliotecaSingletonFacade()
            biblioteca.observarLivro(
                int(self.__restoComando[0]), int(self.__restoComando[1])
            )
        except IndexError:
            console = ConsoleSingleton()
            console.print("Houve um erro no formato do seu comando")
