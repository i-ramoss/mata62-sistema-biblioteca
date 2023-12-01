from ..Usuario.Usuario import Usuario
from ..Reserva.Reserva import Reserva
from ..Livro.Livro import Livro 


class BibliotecaSingletonFacede:
    __instance = None

    #Codigo relacionado a implementação do Singleton em python
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__livros: list[Livro] = []
        self.__usuarios: list[Usuario] = []
        self.__reservas: list[Reserva] = []

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

    def adicionarUsuario(self, codigoUsuario: int, nomeUsuario: str, cargoUsuario: int) -> None:
        if self.__buscarUsuarioPeloCodigo(codigoUsuario) != None:
            novoUsuario = Usuario(codigoUsuario, nomeUsuario, emprestimoBehavior)
            self.__usuarios.append(novoUsuario)


    def __adicionarUsuario(self, novoUsuario: Usuario) -> None:
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

    def realizarDevolucao(self, codigoUsuario: int, codigoLivro: int) -> None:
        pass
    
    def observarLivroProfessor(self, codigoProfessor: int, codigoLivro: int) -> None:
        pass
    
    def mostraNotificaoProfessor(self, codigoProfessor: int) -> None:
        pass
    
    def __criaReserva(self, codigoUsuario:int, codigoLivro:int) -> Reserva:
        usuario = self.__buscarUsuarioPeloCodigo(codigoUsuario)
        livro = self.__buscarLivroPeloCodigo(codigoLivro)
        return Reserva(usuario, livro)

