from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede 

class CommandAddLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(self): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.adicionarLivro(self.__restoComando[0])
