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

class ConsoleSingleton():
    __instance = None
    
    #Codigo relacionado a implementação do Singleton em python
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getConsoleLoop(self):
        userInput = input("> ")
        userInput = userInput.split()
        comando = userInput[0]
        restListInput = userInput[1:]
        if comando == "emp":
            command = CommandEmprestar(restListInput)
        elif comando == "dev":
            command = CommandDevolver(restListInput)
        elif comando == "res":
            command = CommandReservar(restListInput)
        elif comando == "obs":
            command = CommandObservar(restListInput)
        elif comando == "liv":
            command = CommandConsultaLivro(restListInput)
        elif comando == "usu":
            command = CommandConsultaUsuario(restListInput)
        elif comando == "ntf":
            command = CommandNotificaoProfessor(restListInput)
        elif comando == "adu":
            command = CommandAddUser(restListInput)
        elif comando == "adl":
            command = CommandAddLivro(restListInput)
        elif comando == "sai":
            self.print("FuncaoTerminada")
            exit(0)
        try:
            command.execute()
        except NotImplementedError:
            self.error("Funcao nao implementada")

    def print(self, string: str) -> None:
        print(f"[Console logger]: {string}")

    def print(self, string: str) -> None:
        print(f"[Console error]: {string}", file=sys.stderror)
                
