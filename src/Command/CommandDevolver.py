from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede

class CommandDevolver(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(self): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.devolverLivroUsuario(self.__restoComando[0], self.__restoComando[1])
