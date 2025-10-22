class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, me chamo {self.nome} e tenho {self.idade} anos."
    

class Estudante(Pessoa): #Herda da class Pessoa
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}."
    

p1 = Pessoa("João", 40)
print(p1.apresentar())

e1 = Estudante("Maria", 21, "Medicina")
print(e1.apresentar())