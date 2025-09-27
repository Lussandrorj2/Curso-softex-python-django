#herança e lista → Class animal

class Animal():
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} faz o som")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print(f"O {self.nome} faz Miauu..!")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print(f"O {self.nome} faz AUAU!!!")

gato = Gato("Félix")
cachorro = Cachorro("Apolo")

lista = [gato, cachorro]

for animal in lista:
    animal.fazer_som()