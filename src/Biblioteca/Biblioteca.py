from ..Usuario import Usuario
from ..Livro import Livro
from ..Emprestimo import Emprestimo
from ..Reserva import Reserva
from ..Enums import Status


class BibliotecaMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BibliotecaSingletonFacede(metaclass=BibliotecaMeta):
    def __init__(self):
        self.__livros: list[Livro] = []
        self.__usuarios: list[Usuario] = []
        self.__emprestimos: list[Emprestimo] = []
        self.__reservas: list[Reserva] = []

    def adicionarLivro(self, novoLivro: Livro, qtdExemplares: int) -> None:
        livroEncontrado = self.buscarLivroPeloCodigo(novoLivro.getCodigo())

        if livroEncontrado:
            livroEncontrado.setQtdDisponivel(qtdExemplares)
            return
        else:
            novoLivro.setQtdDisponivel(qtdExemplares)
            self.__livros.append(novoLivro)

    def buscarLivroPeloCodigo(self, codigoLivro: int) -> Livro:
        for livro in self.__livros:
            if livro.getCodigo() == codigoLivro:
                return livro

    def adicionarUsuario(self, novoUsuario: Usuario) -> None:
        usuarioEncontrado = self.buscarUsuarioPeloCodigo(novoUsuario.getCodigo())

        if usuarioEncontrado == None:
            self.__usuarios.append(novoUsuario)

    def __adicionarUsuario(self, novoUsuario: Usuario) -> None:
        usuarioEncontrado = self.buscarUsuarioPeloCodigo(novoUsuario.getCodigo())

        if usuarioEncontrado == None:
            self.__usuarios.append(novoUsuario)

    def buscarUsuarioPeloCodigo(self, codigoUsuario: int) -> Usuario:
        for usuario in self.__usuarios:
            if usuario.getCodigo() == codigoUsuario:
                return usuario

    def realizarEmprestimo(self, codigoUsuario: int, codigoLivro: int) -> None:
        usuario = self.buscarUsuarioPeloCodigo(codigoUsuario)
        livro = self.buscarLivroPeloCodigo(codigoLivro)

        # Verificar se o usuário pode realizar empréstimo
        if usuario == None:
            print("O usuario nao esta cadastrado na biblioteca.")
            return

        usuarioPodeRealizarOEmprestimo = usuario.verificarPossibilidadeDeEmprestimo(
            codigoUsuario, codigoLivro
        )

        if not usuarioPodeRealizarOEmprestimo:
            print("O usuario nao pode realizar o emprestimo.")
            return

        # Verificar se o usuário possui reserva para o livro
        reserva = self.buscarReservaDeLivroDoUsuario(codigoUsuario, codigoLivro)

        # Se possuir reserva, exclui e realiza o emprestimo
        if reserva:
            self.__reservas.remove(reserva)

        self.__emprestimos.append(Emprestimo(usuario, livro))

        print("Emprestimo realizado com sucesso.")

    def realizarReserva(self, codigoUsuario: int, codigoLivro: int) -> None:
        # Buscar o usuario e livro pelo codigo, respectivamente
        usuarioEncontrado = self.buscarUsuarioPeloCodigo(codigoUsuario)
        livroEncontrado = self.buscarLivroPeloCodigo(codigoLivro)

        if usuarioEncontrado == None:
            # msg de erro:
            print("Usuario não encontrado. Digite um codigo valido.")
            return

        if livroEncontrado == None:
            # msg de erro:
            print("Livro não encontrado. Digite um codigo valido.")
            return

        # Checar quantas reservas ele possui (maximo 3)
        qtdReservas = len(self.buscarReservasPeloCodigoDoUsuario(codigoUsuario))

        if qtdReservas >= 3:
            # msg de erro:
            print("O usuario ja possui o limite de reservas.")

        # Realizar reserva
        self.__reservas.append(Reserva(usuarioEncontrado, livroEncontrado))

        # msg de sucesso:
        print(
            f"O livro {livroEncontrado.getTitulo()} foi reservado para {usuarioEncontrado.getNome()} com sucesso!"
        )

    def realizarDevolucao(self, codigoUsuario: int, codigoLivro: int) -> None:
        pass

    def buscarReservasPeloCodigoDoUsuario(self, codigoUsuario: int) -> list[Reserva]:
        reservasEncontradas = []

        for reserva in self.__reservas:
            if reserva.getUsuario().getCodigo() == codigoUsuario:
                reservasEncontradas.append(reserva)

        return reservasEncontradas

    def buscarReservasPeloCodigoDoLivro(self, codigoLivro: int) -> list[Reserva]:
        reservasEncontradas = []

        for reserva in self.__reservas:
            if reserva.getLivro().getCodigo() == codigoLivro:
                reservasEncontradas.append(reserva)

        return reservasEncontradas

    def buscarReservaDeLivroDoUsuario(
        self, codigoUsuario: int, codigoLivro: int
    ) -> Reserva:
        for reserva in self.__reservas:
            if (
                reserva.getUsuario().getCodigo() == codigoUsuario
                and reserva.getLivro().getCodigo() == codigoLivro
            ):
                return reserva

    def removerReservaDeLivro(self, codigoUsuario: int, codigoLivro: int):
        for reserva in self.__reservas:
            if (
                reserva.getUsuario().getCodigo() == codigoUsuario
                and reserva.getLivro().getCodigo() == codigoLivro
            ):
                self.__reservas.remove(reserva)

    def buscarEmprestimosPeloCodigoDoUsuario(
        self, codigoUsuario: int
    ) -> list[Emprestimo]:
        emprestimosEncontrados = []

        for emprestimo in self.__emprestimos:
            if emprestimo.getUsuario().getCodigo() == codigoUsuario:
                emprestimosEncontrados.append(emprestimo)

        return emprestimosEncontrados

    def checarEmprestimoAtrasadoUsuario(self, codigoUsuario: int) -> bool:
        emprestimosAluno = self.buscarEmprestimosPeloCodigoDoUsuario(codigoUsuario)

        for emprestimo in emprestimosAluno:
            if emprestimo.getStatus() == Status.ATRASADO:
                return True

        return False

    def observarLivroProfessor(self, codigoProfessor: int, codigoLivro: int) -> None:
        pass

    def mostraNotificaoProfessor(self, codigoProfessor: int) -> None:
        pass


# buscar emprestimo pelo codigo de usuario
# buscar emprestimo pelo codigo de livro

# buscar reserva pelo codigo de usuario
# buscar reserva pelo codigo de livro
