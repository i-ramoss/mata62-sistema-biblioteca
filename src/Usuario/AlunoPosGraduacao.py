from .Usuario import Usuario
from ..EmprestimoBehavior import EmprestimoPosGraduacao


class AlunoPosGraduacao(Usuario):
    def __init__(self, codigo: int, nome: str) -> None:
        super().__init__(codigo, nome, EmprestimoPosGraduacao())
