class Livro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        editora: str,
        autores: list[str],
        edicao: str,
        anoPublicacao: int,
    ) -> None:
        self.__codigo = codigo
        self.__titulo = titulo
        self.__editora = editora
        self.__autores = autores
        self.__edicao = edicao
        self.__anoPublicacao = anoPublicacao
        self.__qtdDisponivel = 1
