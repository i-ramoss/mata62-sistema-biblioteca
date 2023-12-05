from .IEmprestimoBehavior import IEmprestimoBehavior


class EmprestimoProfessor(IEmprestimoBehavior):
    def __init__(self):
        self.__intervaloDeTempoDeEmprestimo = 7

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

        # (ii) Verificar se o professor está devedor
        if biblioteca.checarEmprestimoAtrasadoUsuario(codigoUsuario):
            console.print("O professor possui emprestimo em atraso.")
            return False

        return True

    def getIntervaloDeTempoDeEmprestimo(self) -> int:
        return self.__intervaloDeTempoDeEmprestimo
