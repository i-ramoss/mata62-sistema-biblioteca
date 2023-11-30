class Usuario:
    def __init__(self, codigo: int, nome: str, ) -> None:
        self._codigo = codigo
        self._nome = nome

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_intervalo_emprestimo(self):
        return self.__intervalo_emprestimo
