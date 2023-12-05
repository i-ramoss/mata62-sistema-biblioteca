from .ICommand import ICommand


class CommandAddUser(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        from ..Biblioteca import BibliotecaSingletonFacade

        biblioteca = BibliotecaSingletonFacade()
        biblioteca.adicionarUsuario(self.__restoComando[0])
