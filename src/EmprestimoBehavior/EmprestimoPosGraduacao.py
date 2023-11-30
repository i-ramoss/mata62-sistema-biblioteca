from .IEmprestimoBehavior import IEmprestimoBehavior


class EmprestimoPosGraduacao(IEmprestimoBehavior):
    __intervaloDeTempoDeEmprestimo = 4

    def verificarPossibilidadeDeEmprestimo():
        # Verificar disponibilidade do livro na biblioteca
        # Verificar se o aluno está devedor
        # Verificar o limite de emprestimo do aluno
        # Verificar se o aluno possui reserva do livro
        # Se sim e houver livro disponivel ele pode pegar emprestado
        # Se não, checar se o número de reservas do livro é menor do que a quantidade de livros disponíveis, se sim, ele pode pegar emprestado
        # Verificar se o aluno já não possui o livro em questão emprestado
        print("Regra emprestimo pos-graducacao")
        pass
