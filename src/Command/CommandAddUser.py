from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede 

class CommandAddUser(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.adicionarUsuario(self.__restoComando[0], self.__restoComando[1], self.__restoComando[2])
