class Filme():
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"Filme: {self.titulo} ano {self.ano} - Diretor: {self.diretor}"
    
filme1 = Filme("De volta para o futuro", "Robert Zemeckis", 1985)
print(filme1)