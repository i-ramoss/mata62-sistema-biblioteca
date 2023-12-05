from .IEmprestimoBehavior import IEmprestimoBehavior


class EmprestimoPosGraduacao(IEmprestimoBehavior):
    def __init__(self):
        self.__intervaloDeTempoDeEmprestimo = 4
        self.__limiteDeEmprestimosEmAberto = 4

    def verificarPossibilidadeDeEmprestimo(
        self, codigoUsuario: int, codigoLivro: int
    ) -> bool:
        from ..Biblioteca import BibliotecaSingletonFacade
        from ..Console import ConsoleSingleton

        biblioteca = BibliotecaSingletonFacade()
        console = ConsoleSingleton()

        # (i) Verificar disponibilidade do livro na biblioteca
        livro = biblioteca.buscarLivroPeloCodigo(codigoLivro)

        if livro == None:
            console.print("O livro nao esta cadastrado na biblioteca.")
            return False
        if livro.getQtdDisponivel() <= 0:
            console.print("O livro não está disponivel.")
            return False

        # (ii) Verificar se o aluno está devedor
        if biblioteca.checarEmprestimoAtrasadoUsuario(codigoUsuario):
            console.print("O aluno possui emprestimo em atraso.")
            return False

        # (iii) Verificar o limite de emprestimo do aluno
        emprestimosAluno = biblioteca.buscarEmprestimosPeloCodigoDoUsuario(
            codigoUsuario
        )

        if len(emprestimosAluno) >= self.__limiteDeEmprestimosEmAberto:
            console.print(
                "O aluno atingiu a quantidade máxima de emprestimos em aberto."
            )
            return False

        # (iv) Verificar se o aluno possui reserva do livro
        reservaRealizada = biblioteca.buscarReservaDeLivroDoUsuario(
            codigoUsuario, codigoLivro
        )

        # (v) Se não possui, checar se o número de reservas do livro é menor do que a quantidade de livros disponíveis, se sim, ele pode pegar emprestado
        if reservaRealizada != None:
            if livro.getQtdDisponivel() <= len(
                biblioteca.buscarReservasPeloCodigoDoLivro(codigoLivro)
            ):
                console.print(
                    "O livro ja possui reservas e nao ha exemplares adicionais disponiveis."
                )
                return False

        # (vi) Verificar se o aluno já não possui o livro em questão emprestado
        for emprestimo in emprestimosAluno:
            if emprestimo.getLivro().getCodigo() == codigoLivro:
                console.print("O usuario ja possui este livro emprestado.")
                return False

        return True

    def getIntervaloDeTempoDeEmprestimo(self) -> int:
        return self.__intervaloDeTempoDeEmprestimo
