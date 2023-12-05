from src import (
    AlunoGraduacao,
    AlunoPosGraduacao,
    Professor,
    BibliotecaSingletonFacade,
    Livro,
    ConsoleSingleton,
)

usuarios = [
    AlunoGraduacao(123, "Flora Ramos"),
    AlunoGraduacao(456, "Cecília Ramos"),
    AlunoPosGraduacao(789, "Ninna Simas"),
    Professor("100", "Carlos Sant'Anna"),
]

livros = [
    {
        "codigo": 100,
        "titulo": "Engenharia de Software",
        "editora": "AddisonWesley",
        "autores": ["Ian Sommmervile"],
        "edicao": "6ª",
        "anoPublicacao": 2000,
        "qtdExemplares": 5,
    }
]

biblioteca = BibliotecaSingletonFacade()

for usuario in usuarios:
    biblioteca.adicionarUsuario(usuario)

for livro in livros:
    novoLivro = Livro(
        livro.get("codigo"),
        livro.get("titulo"),
        livro.get("editora"),
        livro.get("autores"),
        livro.get("edicao"),
        livro.get("anoPublicacao"),
    )

    biblioteca.adicionarLivro(novoLivro, livro.get("qtdExemplares"))


# biblioteca.realizarReserva(usuario1.getCodigo(), engSoftSommervile.getCodigo())
# biblioteca.realizarEmprestimo(usuario1.getCodigo(), engSoftSommervile.getCodigo())
# biblioteca.realizarEmprestimo(usuario2.getCodigo(), engSoftSommervile.getCodigo())
# biblioteca.realizarDevolucao(usuario2.getCodigo(), engSoftSommervile.getCodigo())

# biblioteca.consultarLivro(engSoftSommervile.getCodigo())
# biblioteca.consultarUsuario(usuario1.getCodigo())

console = ConsoleSingleton()
console.getConsoleLoop()
