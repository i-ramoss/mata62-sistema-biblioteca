from ..Usuario import Usuario
from ..Livro import Livro
from ..Emprestimo import Emprestimo
from ..Reserva import Reserva
from ..Enums import StatusEmprestimo, StatusExemplar
from ..Console import ConsoleSingleton


class BibliotecaMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BibliotecaSingletonFacade(metaclass=BibliotecaMeta):
    def __init__(self):
        self.__livros: list[Livro] = []
        self.__usuarios: list[Usuario] = []
        self.__emprestimos: list[Emprestimo] = []
        self.__reservas: list[Reserva] = []

    def adicionarLivro(self, novoLivro: Livro, qtdExemplares: int) -> None:
        livro = self.buscarLivroPeloCodigo(novoLivro.getCodigo())
        if livro:
            livro.criarExemplares(qtdExemplares)
            return
        else:
            novoLivro.criarExemplares(qtdExemplares - 1)
            self.__livros.append(novoLivro)

    def adicionarUsuario(self, novoUsuario: Usuario) -> None:
        usuarioEncontrado = self.buscarUsuarioPeloCodigo(novoUsuario.getCodigo())

        if usuarioEncontrado == None:
            self.__usuarios.append(novoUsuario)

    def realizarEmprestimo(self, codigoUsuario: int, codigoLivro: int) -> None:
        usuario = self.buscarUsuarioPeloCodigo(codigoUsuario)
        livro = self.buscarLivroPeloCodigo(codigoLivro)
        console = ConsoleSingleton()
        
        if usuario == None:
            console.print("O usuario nao esta cadastrado na biblioteca.")
            return

        # Verificar se o usuário pode realizar empréstimo
        usuarioPodeRealizarOEmprestimo = usuario.verificarPossibilidadeDeEmprestimo(
            codigoUsuario, codigoLivro
        )

        if not usuarioPodeRealizarOEmprestimo:
            console.print("O usuario nao pode realizar o emprestimo.")
            return

        # Verificar se o usuário possui reserva para o livro
        reserva = self.buscarReservaDeLivroDoUsuario(codigoUsuario, codigoLivro)

        # Se possuir reserva, exclui e realiza o emprestimo
        if reserva:
            self.__reservas.remove(reserva)

        self.__emprestimos.append(Emprestimo(usuario, livro))

        console.print(
            f"O livro {livro.getTitulo()} foi emprestado para {usuario.getNome()} com sucesso!"
        )

    def realizarReserva(self, codigoUsuario: int, codigoLivro: int) -> None:
        # Buscar o usuario e livro pelo codigo, respectivamente
        usuario = self.buscarUsuarioPeloCodigo(codigoUsuario)
        livro = self.buscarLivroPeloCodigo(codigoLivro)
        console = ConsoleSingleton()

        if usuario == None:
            # msg de erro:
            console.print("Usuario não encontrado. Digite um codigo valido.")
            return

        if livro == None:
            # msg de erro:
            console.print("Livro não encontrado. Digite um codigo valido.")
            return

        # Checar quantas reservas ele possui (maximo 3)
        qtdReservas = len(self.buscarReservasPeloCodigoDoUsuario(codigoUsuario))

        if qtdReservas >= 3:
            # msg de erro:
            console.print("O usuario ja possui o limite de reservas.")

        # Realizar reserva
        self.__reservas.append(Reserva(usuario, livro))

        # msg de sucesso:
        console.print(
            f"O livro {livro.getTitulo()} foi reservado para {usuario.getNome()} com sucesso!"
        )

    def realizarDevolucao(self, codigoUsuario: int, codigoLivro: int) -> None:
        # Buscar o usuario e livro pelo codigo, respectivamente
        usuario = self.buscarUsuarioPeloCodigo(codigoUsuario)
        console = ConsoleSingleton()
        livro = self.buscarLivroPeloCodigo(codigoLivro)

        if usuario == None:
            # msg de erro:
            console.print("Usuario não encontrado. Digite um codigo valido.")
            return

        if livro == None:
            # msg de erro:
            console.print("Livro não encontrado. Digite um codigo valido.")
            return

        emprestimosUsuario = self.buscarEmprestimosPeloCodigoDoUsuario(codigoUsuario)

        emprestimoASerFinalizado = None

        for emprestimo in emprestimosUsuario:
            if emprestimo.getLivro().getCodigo() == codigoLivro and (
                emprestimo.getStatus() == StatusEmprestimo.EM_ANDAMENTO
                or emprestimo.getStatus() == StatusEmprestimo.ATRASADO
            ):
                emprestimoASerFinalizado = emprestimo

        if emprestimoASerFinalizado == None:
            console.print("O usuario nao possui emprestimo em aberto para este livro.")
            return

        else:
            emprestimoASerFinalizado.finalizar()
            console.print(
                f"O livro {livro.getTitulo()}, emprestado para {usuario.getNome()}, foi devolvido  com sucesso!"
            )

    def consultarLivro(self, codigoLivro: int):
        livro = self.buscarLivroPeloCodigo(codigoLivro)
        console = ConsoleSingleton()

        if livro == None:
            # msg de erro:
            console.print("Livro não encontrado. Digite um codigo valido.")
            return

        reservas = self.buscarReservasPeloCodigoDoLivro(codigoLivro)

        console.print(f"Titulo do livro: {livro.getTitulo()}")
        console.print(f"Quantidade de reservas: {len(reservas)}")

        if len(reservas) > 0:
            for reserva in reservas:
                console.print(f"Reserva realizada por {reserva.getUsuario().getNome()}.")

        emprestimos = self.buscarEmprestimosPeloCodigoDoLivro(codigoLivro)

        console.print()
        console.print(f"Quantidade de emprestimos: {len(emprestimos)}")
        for exemplar in livro.listarExemplares():
            console.print(
                f"Exemplar: {exemplar.getCodigo()} - Status: {exemplar.getStatus().value}"
            )

            if exemplar.getStatus() == StatusExemplar.EMPRESTADO:
                for emprestimo in emprestimos:
                    if exemplar.getCodigo() == emprestimo.getCodigoExemplar():
                        console.print(
                            f"Emprestimo realizado por: {emprestimo.getUsuario().getNome()}. De {emprestimo.getDataInicio()} a {emprestimo.getDataDevolucao()}"
                        )

    def consultarUsuario(self, codigoUsuario: int):
        console = ConsoleSingleton()
        usuario = self.buscarUsuarioPeloCodigo(codigoUsuario)

        if usuario == None:
            # msg de erro:
            console.print("Usuario não encontrado. Digite um codigo valido.")
            return

        emprestimos = self.buscarEmprestimosPeloCodigoDoUsuario(codigoUsuario)
        reservas = self.buscarReservasPeloCodigoDoUsuario(codigoUsuario)

        console.print(f"Emprestimos: {len(emprestimos)}")
        for emprestimo in emprestimos:
            console.print(f"Titulo: {emprestimo.getLivro().getTitulo()}")
            console.print(
                f"Data: {emprestimo.getDataInicio()} - {emprestimo.getDataDevolucao()}"
            )
            console.print(f"Status: {emprestimo.getStatus().value}")

        console.print()
        console.print(f"Reservas: {len(reservas)}")
        for reserva in reservas:
            console.print(f"Titulo: {reserva.getLivro().getTitulo()}")
            console.print(f"Data solicitacao: {reserva.getDataSolicitacao()}")

    def __adicionarUsuario(self, novoUsuario: Usuario) -> None:
        usuarioEncontrado = self.buscarUsuarioPeloCodigo(novoUsuario.getCodigo())

        if usuarioEncontrado == None:
            self.__usuarios.append(novoUsuario)

    def buscarLivroPeloCodigo(self, codigoLivro: int) -> Livro:
        for livro in self.__livros:
            if livro.getCodigo() == codigoLivro:
                return livro

    def buscarUsuarioPeloCodigo(self, codigoUsuario: int) -> Usuario:
        for usuario in self.__usuarios:
            if usuario.getCodigo() == codigoUsuario:
                return usuario

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

    def buscarEmprestimosPeloCodigoDoLivro(self, codigoLivro: int) -> list[Emprestimo]:
        emprestimosEncontrados = []

        for emprestimo in self.__emprestimos:
            if emprestimo.getLivro().getCodigo() == codigoLivro:
                emprestimosEncontrados.append(emprestimo)

        return emprestimosEncontrados

    def checarEmprestimoAtrasadoUsuario(self, codigoUsuario: int) -> bool:
        emprestimosAluno = self.buscarEmprestimosPeloCodigoDoUsuario(codigoUsuario)

        for emprestimo in emprestimosAluno:
            if emprestimo.getStatus() == StatusEmprestimo.ATRASADO:
                return True

        return False

    def observarLivroProfessor(self, codigoProfessor: int, codigoLivro: int) -> None:
        console = ConsoleSingleton()
        livro = self.buscarLivroPeloCodigo(codigoLivro)
        professor = self.buscarUsuarioPeloCodigo(codigoProfessor)
        livro.subscribe(professor)
        pass

    def mostraNotificaoProfessor(self, codigoProfessor: int) -> None:
        console = ConsoleSingleton()
        professor = self.buscarUsuarioPeloCodigo(codigoProfessor)
        console.print(f"O número de vezes em que o professor foi notificado é: {professor.getVezesNotificado()}")
