from ..Command.ICommand import ICommand 
from ..Command.CommandEmprestar import CommandEmprestar
from ..Command.CommandAddLivro import CommandAddLivro
from ..Command.CommandAddUser import CommandAddUser
from ..Command.CommandObservar import CommandObservar
from ..Command.CommandReservar import CommandReservar
from ..Command.CommandDevolver import CommandDevolver
from ..Command.CommandConsultaLivro import CommandConsultaLivro
from ..Command.CommandConsultaUsuario import CommandConsultaUsuario
from ..Command.CommandNotificaoProfessor import CommandNotificacaoProfessor
import sys
from abc import ABC, abstractmethod

class ConsoleMeta(type):
    #Codigo relacionado a implementação do Singleton em python
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class ConsoleSingleton(metaclass=ConsoleMeta):
    def __init__(self):
        self.__comando = {
                "emp": CommandEmprestar,
                "dev": CommandDevolver,
                "res": CommandReservar,
                "obs": CommandObservar,
                "lib": CommandConsultaLivro,
                "usu": CommandConsultaUsuario,
                "ntf": CommandNotificacaoProfessor,
                }

    
    def getConsoleLoop(self):
        userInput = input("> ")
        userInput = userInput.split()
        comando = userInput[0]
        restListInput = userInput[1:]
        try:
            command = self.__comando[comando](restListInput)
            if comando == "sai":
                self.print("FuncaoTerminada")
            exit(0)
            command.execute()
        except NotImplementedError:
            self.error("Funcao nao implementada")

    def print(self, string: str) -> None:
        print(f"[Console logger]: {string}")

    def print(self, string: str) -> None:
        print(f"[Console error]: {string}", file=sys.stderror)
                
