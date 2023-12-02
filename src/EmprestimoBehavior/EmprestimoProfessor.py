from .IEmprestimoBehavior import IEmprestimoBehavior
from ..Biblioteca import BibliotecaSingletonFacade


class EmprestimoProfessor(IEmprestimoBehavior):
    def __init__(self):
        self.__intervaloDeTempoDeEmprestimo = 7

    def verificarPossibilidadeDeEmprestimo(
        self, codigoUsuario: int, codigoLivro: int
    ) -> bool:
        biblioteca = BibliotecaSingletonFacade()

        # (i) Verificar disponibilidade do livro na biblioteca
        livro = biblioteca.buscarLivroPeloCodigo(100)

        if livro == None:
            print("O livro nao esta cadastrado na biblioteca.")  # msg console
            return False
        if livro.getQtdDisponivel() <= 0:
            print("O livro não está disponivel.")  # msg console
            return False

        # (ii) Verificar se o professor está devedor
        if biblioteca.checarEmprestimoAtrasadoUsuario(codigoUsuario):
            print("O professor possui emprestimo em atraso.")  # msg console
            return False

        return True

    def getIntervaloDeTempoDeEmprestimo(self) -> int:
        return self.__intervaloDeTempoDeEmprestimo
