from .ICommand import ICommand

class CommandConsultaUsuario(ICommand):
    def __init__(self, restoComando):
        self.__restoComando =  restoComando

    def execute(): 
        Facade.ConsultaLivro(self.__restoComando[0])
