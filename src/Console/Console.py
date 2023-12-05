import sys

from ..Command import ICommand
from ..Command import CommandEmprestar
from ..Command import CommandAddLivro
from ..Command import CommandAddUser
from ..Command import CommandObservar
from ..Command import CommandReservar
from ..Command import CommandDevolver
from ..Command import CommandConsultaLivro
from ..Command import CommandConsultaUsuario
from ..Command import CommandNotificacaoProfessor


class ConsoleMeta(type):
    # Codigo relacionado a implementação do Singleton em python
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class ConsoleSingleton(metaclass=ConsoleMeta):
    def __init__(self):
        self.__comando: ICommand = {
            "emp": CommandEmprestar,
            "dev": CommandDevolver,
            "res": CommandReservar,
            "obs": CommandObservar,
            "lib": CommandConsultaLivro,
            "usu": CommandConsultaUsuario,
            "ntf": CommandNotificacaoProfessor,
            "adu": CommandAddUser,
            "adl": CommandAddLivro,
        }

    def getConsoleLoop(self):
        userInput = input("> ")
        userInput = userInput.split()
        comando = userInput[0]
        restListInput = userInput[1:]
        try:
            if comando == "sai":
                self.print("Saiu do programa.")
                exit(0)

            command = self.__comando[comando](restListInput)
            command.execute()
        except NotImplementedError:
            self.error("Funcao nao implementada")

    def print(self, string: str) -> None:
        print(f"[Console logger]: {string}")

    def printerr(self, string: str) -> None:
        print(f"[Console error]: {string}", file=sys.stderr)
