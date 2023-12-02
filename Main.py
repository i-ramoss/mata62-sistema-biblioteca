from src import (
    AlunoGraduacao,
    BibliotecaSingletonFacade,
    Livro,
)


usuario1 = AlunoGraduacao(123, "Flora Ramos")
usuario2 = AlunoGraduacao(456, "Cecília Ramos")

engSoftSommervile = Livro(
    100, "Engenharia de Software", "AddisonWesley", ["Ian Sommmervile"], "6ª", 2000
)

biblioteca = BibliotecaSingletonFacade()
biblioteca.adicionarUsuario(usuario1)

biblioteca.adicionarLivro(engSoftSommervile, 5)

biblioteca.realizarReserva(usuario1.getCodigo(), engSoftSommervile.getCodigo())
biblioteca.realizarEmprestimo(usuario1.getCodigo(), engSoftSommervile.getCodigo())
biblioteca.realizarDevolucao(usuario1.getCodigo(), engSoftSommervile.getCodigo())
