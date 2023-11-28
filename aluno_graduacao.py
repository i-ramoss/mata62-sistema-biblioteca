from usuario import Usuario


class AlunoGraduacao(Usuario):
    def __init__(self, codigo: int, nome: str, intervalo_emprestimo: int):
        super().__init__(codigo, nome, intervalo_emprestimo)
