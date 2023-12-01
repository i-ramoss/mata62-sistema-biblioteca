from src import (
    Usuario,
    EmprestimoPosGraduacao,
    EmprestimoProfessor,
    BibliotecaSingletonFacede,
    Livro,
)


usuario1 = Usuario(123, "Flora Ramos", EmprestimoPosGraduacao)
usuario2 = Usuario(456, "Cecília Ramos", EmprestimoProfessor)

engSoftSommervile = Livro(
    100, "Engenharia de Software", "AddisonWesley", ["Ian Sommmervile"], "6ª", 2000
)

biblioteca = BibliotecaSingletonFacede()
biblioteca.adicionarUsuario(usuario1)
biblioteca.adicionarLivro(engSoftSommervile, 5)


print("Qtd exemplares", engSoftSommervile.getQtdDisponivel())

biblioteca.realizarReserva(usuario1.getCodigo(), engSoftSommervile.getCodigo())
