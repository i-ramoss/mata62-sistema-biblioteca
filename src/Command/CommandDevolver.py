from .ICommand import ICommand

class CommandDevolver(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        Facade.DevolverLivroUsuario(self.__restoComando[0], self.__restoComando[1])
