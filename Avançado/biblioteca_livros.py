class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    

class Biblioteca():
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def listar_livros(self):
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            for livro in self.acervo:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}")

biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()