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
    Professor(100, "Carlos Sant'Anna"),
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
    },
    {
        "codigo": 101,
        "titulo": "UML - Guia do Usuário",
        "editora": "Campus",
        "autores": ["Grady Booch", "James Rumbaugh", "Ivar Jacobson"],
        "edicao": "7ª",
        "anoPublicacao": 2000,
        "qtdExemplares": 1,
    },
    {
        "codigo": 200,
        "titulo": "Code Complete",
        "editora": "Microsoft Press",
        "autores": ["Steve McConnell"],
        "edicao": "2ª",
        "anoPublicacao": 2014,
        "qtdExemplares": 1,
    },
    {
        "codigo": 201,
        "titulo": "Agile Software Development, Principles, Patterns, and Practices",
        "editora": "Prentice Hall",
        "autores": ["Robert Martin"],
        "edicao": "1ª",
        "anoPublicacao": 2002,
        "qtdExemplares": 1,
    },
    {
        "codigo": 300,
        "titulo": "Refactoring: Improving the Design of Existing Code",
        "editora": "Addison-Wesley Professional",
        "autores": ["Martin Fowler"],
        "edicao": "1ª",
        "anoPublicacao": 1999,
        "qtdExemplares": 2,
    },
    {
        "codigo": 301,
        "titulo": "Software Metrics: A Rigorous and Practical Approach",
        "editora": "CRC Press",
        "autores": ["Norman Fenton", "James Bieman"],
        "edicao": "3ª",
        "anoPublicacao": 2014,
        "qtdExemplares": 1,
    },
    {
        "codigo": 400,
        "titulo": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "editora": "Addison-Wesley Professional",
        "autores": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
        "edicao": "1ª",
        "anoPublicacao": 1994,
        "qtdExemplares": 2,
    },
    {
        "codigo": 401,
        "titulo": "UML Distilled: A Brief Guide to the Standard Object Modeling Language",
        "editora": "Addison-Wesley Professional",
        "autores": ["Martin Fowler"],
        "edicao": "3ª",
        "anoPublicacao": 2003,
        "qtdExemplares": 1,
    },
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

console = ConsoleSingleton()
console.getConsoleLoop()
