from .ICommand import ICommand


class CommandSair(ICommand):
    def __init__(self, restoComando):
        self.__restoComando = restoComando

    def execute(self):
        print("[Console logger]: Saiu do programa.")
        exit(0)
