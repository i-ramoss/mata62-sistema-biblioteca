from .EmprestimoBehaviour import EmprestimoAluno

class Usuario:
    def __init__(self, codigo: int, nome: str, emprestimoBehaviour: EmprestimoAluno) -> None:
        self._codigo = codigo
        self._nome = nome
        self._emprestimoBehaviour = emprestimoBehaviour(self)

    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome
