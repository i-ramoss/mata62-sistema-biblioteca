from enum import Enum


class StatusEmprestimo(Enum):
    EM_ANDAMENTO = "Em andamento"
    FINALIZADO = "Finalizado"
    ATRASADO = "Atrasado"
