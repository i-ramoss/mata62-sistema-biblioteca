from .Usuario import Usuario
from ..EmprestimoBehavior import EmprestimoProfessor


class Professor(Usuario):
    def __init__(self, codigo: int, nome: str) -> None:
        super().__init__(codigo, nome, EmprestimoProfessor())
