class Comodo:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome

class Casa:
    def __init__(self, lista_comodos):
        self.comodos = []
        if self.comodos:
            for nome in lista_comodos:
                self.adicionar_comodo(nome)

    def adicionar_comodo(self, nome):
        comodo = Comodo(nome)
        self.comodos.append(comodo)

    def listar_comodos(self):
        print("Cômodos da casa")
        for comodo in self.comodos:
            print(f"-{comodo}")

casa = Casa(["Quarto", "Sala"])
casa.adicionar_comodo("Cozinha")
casa.listar_comodos()
casa.adicionar_comodo("Banheiro")
casa.listar_comodos()