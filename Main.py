from src import Usuario, EmprestimoPosGraduacao, EmprestimoProfessor, Biblioteca, Livro


usuario1 = Usuario(123, "Flora Ramos", EmprestimoPosGraduacao)
usuario2 = Usuario(456, "Cecília Ramos", EmprestimoProfessor)

usuario1.getEmprestimoBehavior()
usuario2.getEmprestimoBehavior()


eng_soft_sommervile = Livro(
    100, "Engenharia de Software", "AddisonWesley", ["Ian Sommmervile"], "6ª", 2000
)

biblioteca = Biblioteca()
biblioteca.adicionarLivro(eng_soft_sommervile, 5)


livroEncontrado = biblioteca.buscarLivroPeloCodigo(eng_soft_sommervile.getCodigo())

print("Qtd exemplares", eng_soft_sommervile.getQtdDisponivel())
