from .ICommand import ICommand

class CommandNotificacaoProfessor(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        Facade.NotificacaoProfessor(self.__restoComando[0])
