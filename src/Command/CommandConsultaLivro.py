from .ICommand import ICommand


class CommandConsultaLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade
        from ..Console import ConsoleSingleton
        try:
            biblioteca = BibliotecaSingletonFacade()
            biblioteca.consultarLivro(int(self.__restoComando[0]))
        except IndexError:
            console.print("Houve um erro no formato do seu comando")

