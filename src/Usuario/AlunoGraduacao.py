from .Usuario import Usuario
from ..EmprestimoBehavior import EmprestimoGraduacao


class AlunoGraduacao(Usuario):
    def __init__(self, codigo: int, nome: str) -> None:
        super().__init__(codigo, nome, EmprestimoGraduacao())
