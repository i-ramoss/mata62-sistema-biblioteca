from ..Livro import Livro
from ..Usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.__livros: list[Livro] = []
        self.__usuarios: list[Usuario] = []

    def adicionarLivro(self, novoLivro: Livro, qtdExemplares: int) -> None:
        livroEncontrado = self.__buscarLivroPeloCodigo(novoLivro.getCodigo())

        if livroEncontrado:
            livroEncontrado.setQtdDisponivel(qtdExemplares)
            return
        else:
            novoLivro.setQtdDisponivel(qtdExemplares)
            self.__livros.append(novoLivro)

    def __buscarLivroPeloCodigo(self, codigoLivro: int) -> Livro:
        for livro in self.__livros:
            if livro.getCodigo() == codigoLivro:
                return livro

    def adicionarUsuario(self, novoUsuario: Usuario) -> None:
        usuarioEncontrado = self.__buscarUsuarioPeloCodigo(novoUsuario.getCodigo())

        if usuarioEncontrado == None:
            self.__usuarios.append(novoUsuario)

    def __buscarUsuarioPeloCodigo(self, codigoUsuario: int) -> Usuario:
        for usuario in self.__usuarios:
            if usuario.getCodigo() == codigoUsuario:
                return usuario

    def realizarEmprestimo(self) -> None:
        # Verificar se o usuário possui reserva para o livro
        # Se possuir reserva, exclui e realiza o emprestimo
        # Se não possuir, verificar se há disponibilidade do livro e realiza o emprestimo
        #
        pass

    def realizarReserva(self):
        pass

    def realizarDevolucao(self):
        pass
