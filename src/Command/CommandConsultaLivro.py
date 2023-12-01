from .ICommand import ICommand
from ..Biblioteca.Biblioteca import BibliotecaSingletonFacede

class CommandConsultaLivro(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(self): 
        biblioteca = BibliotecaSingletonFacede()
        biblioteca.consultaLivro(self.__restoComando[0])
