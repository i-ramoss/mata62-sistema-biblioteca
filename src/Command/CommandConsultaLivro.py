from .ICommand import ICommand


class CommandConsultaLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade
        biblioteca = BibliotecaSingletonFacade()
        biblioteca.consultaLivro(self.__restoComando[0])
