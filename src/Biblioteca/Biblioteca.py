from ..Livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar_livro(self, livro: Livro):
        self.__livros.append(livro)

    def realizarEmprestimo(self):
        # Verificar se o usuário possui reserva para o livro
        # Se possuir reserva, exclui e realiza o emprestimo
        # Se não possuir, verificar se há disponibilidade do livro e realiza o emprestimo
        #
        pass

    def realizarReserva(self):
        pass

    def realizarDevolucao(self):
        pass
