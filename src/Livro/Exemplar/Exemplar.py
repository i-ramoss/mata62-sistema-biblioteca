from src.Enums import StatusExemplar


class Exemplar:
    def __init__(self, codigo: int):
        self.__codigo = codigo
        self.__status = StatusExemplar.DISPONIVEL

    def getCodigo(self) -> int:
        return self.__codigo

    def getStatus(self) -> StatusExemplar:
        return self.__status

    def setStatus(self, novoStatus: StatusExemplar) -> None:
        self.__status = novoStatus
