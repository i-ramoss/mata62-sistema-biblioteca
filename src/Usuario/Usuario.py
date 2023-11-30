class Usuario:
    def __init__(self, codigo: int, nome: str, intervaloEmprestimo: int) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__intervaloEmprestimo = intervaloEmprestimo

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getIntervaloEmprestimo(self):
        return self.__intervaloEmprestimo
