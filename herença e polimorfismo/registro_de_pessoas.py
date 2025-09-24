class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")
    
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos, e estou cursando {self.curso}.")


pessoa = Pessoa("João",35)
estudante = Estudante("Joel", 20, "Backend Python")

lista_familia = [pessoa, estudante]
for i in lista_familia:
    i.apresentar()


    