from ..Command import ICommand, CommandEmprestar, CommandDevolver, CommandReservar, CommandObservar, CommandConsultaLivro, CommandConsultaUsuario, CommandNotificaoProfessor
import sys

class ConsoleSingleton():
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getConsoleLoop():
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
        elif comando == "nft":
            command = CommandNotificaoProfessor(restListInput)
        elif comando == "sai":
            self.print("FuncaoTerminada")
            exit(0)
        try:
            command.execute()
        except NotImplemented:
            self.error("Funcao nao implementada")

    def print(self, string: str) -> None:
        print(f"[Console logger]: {string}")

    def print(self, string: str) -> None:
        print(f"[Console error]: {string}", file=sys.stderror)
                
