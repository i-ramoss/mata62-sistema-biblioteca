from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede

class CommandObservar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.observarLivroProfessor(self.__restoComando[0], self.__restoComando[1])
