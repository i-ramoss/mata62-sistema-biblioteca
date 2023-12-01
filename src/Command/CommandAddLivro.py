from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede 

class CommandConsultaLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.adicionarLivro(self.__restoComando[0])
