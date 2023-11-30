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

    def realizarReserva(self, codigoUsuario: int, codigoLivro: int) -> None:
        # Buscar o usuario pelo codigo
        usuario_encontrado = self.__buscarUsuarioPeloCodigo(codigoUsuario)
        livroEncontrado = self.__buscarLivroPeloCodigo(codigoLivro)

        if usuario_encontrado == None:
            # msg de erro:
            print("Usuario não encontrado. Digite um codigo valido.")
            return

        if livroEncontrado == None:
            # msg de erro:
            print("Livro não encontrado. Digite um codigo valido.")
            return

        # Checar quantas reservas ele possui (maximo 3)
        if usuario_encontrado.getQtdReservas() >= 3:
            # msg de erro:
            print("O usuario ja possui o limite de reservas.")

        # Realizar reserva
        usuario_encontrado.adicionarReserva()
        livroEncontrado.adicionarReserva()

        # msg de sucesso:
        print(
            f"O livro {livroEncontrado.getTitulo()} foi reservado para {usuario_encontrado.getNome()} com sucesso!"
        )

    def realizarDevolucao(self) -> None:
        pass
