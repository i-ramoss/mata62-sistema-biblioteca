class Usuario:
    def __init__(self, codigo: int, nome: str, intervalo_emprestimo: int) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__intervalo_emprestimo = intervalo_emprestimo

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_intervalo_emprestimo(self):
        return self.__intervalo_emprestimo
