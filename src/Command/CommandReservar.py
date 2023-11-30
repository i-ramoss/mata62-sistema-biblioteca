from .ICommand import ICommand

class CommandReservar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        Facade.ReservarLivroUsuario(self.__restoComando[0], self.__restoComando[1])
