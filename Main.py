from src import AlunoGraduacao, BibliotecaSingletonFacade, Livro


usuario1 = AlunoGraduacao(123, "Flora Ramos")
usuario2 = AlunoGraduacao(456, "Cecília Ramos")

engSoftSommervile = Livro(
    100, "Engenharia de Software", "AddisonWesley", ["Ian Sommmervile"], "6ª", 2000
)

biblioteca = BibliotecaSingletonFacade()

biblioteca.adicionarUsuario(usuario1)
biblioteca.adicionarUsuario(usuario2)
biblioteca.adicionarLivro(engSoftSommervile, 2)

biblioteca.realizarReserva(usuario1.getCodigo(), engSoftSommervile.getCodigo())
biblioteca.realizarEmprestimo(usuario1.getCodigo(), engSoftSommervile.getCodigo())
biblioteca.realizarEmprestimo(usuario2.getCodigo(), engSoftSommervile.getCodigo())
# biblioteca.realizarDevolucao(usuario2.getCodigo(), engSoftSommervile.getCodigo())

biblioteca.consultarLivro(engSoftSommervile.getCodigo())
# biblioteca.consultarUsuario(usuario1.getCodigo())
