class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Nome: {self.nome}, idade: {self.idade} anos"
    
pessoa1 = Pessoa("João", 36)
print(pessoa1)
