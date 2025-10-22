class Filme():
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f" █ Filme: {self.titulo} | Ano: {self.ano} | Diretor: {self.diretor}"
    
filme1 = Filme("De volta para o futuro", "Robert Zemeckis █", 1985)
filme2 = Filme("Os Goonies", "Richard Donner █", 1985 )
filme3 = Filme("Matrix", " Lilly Wachowski e Lana Wachowski", 1999)
print("~"*70)
print(filme1)
print("~"*70)
print(filme2)
print("~"*70)
print(filme3)
print("~"*70)