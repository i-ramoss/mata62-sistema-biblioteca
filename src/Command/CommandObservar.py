from .ICommand import ICommand

class CommandObservar(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        Facade.ObservarLivroProfessor(self.__restoComando[0], self.__restoComando[1])
