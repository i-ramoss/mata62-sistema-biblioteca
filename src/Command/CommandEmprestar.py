from .ICommand import ICommand

class CommandEmprestar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        Facade.EmprestaLivroUsuario(self.__restoComando[0], self.__restoComando[1])
