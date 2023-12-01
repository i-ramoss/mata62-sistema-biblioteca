from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede

class CommandEmprestar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.realizarEmprestimo(self.__restoComando[0], self.__restoComando[1])
