class Livro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        editora: str,
        autores: list[str],
        edicao: str,
        ano_publicacao: int,
    ) -> None:
        self.__codigo = codigo
        self.__titulo = titulo
        self.__editora = editora
        self.__autores = autores
        self.__edicao = edicao
        self.__ano_publicacao = ano_publicacao
        self.__qtd_disponivel = 1
