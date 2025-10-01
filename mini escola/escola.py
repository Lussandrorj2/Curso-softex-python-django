from classestudante import Estudante

class Escola:
    def __init__(self):
        self.lista_estudante:list[Estudante] = []

    def adicionar_estudante(self, estudante):
        self.lista_estudante.append(estudante)

    def mostrar_lista(self):
        for i in self.lista_estudante:
            print(f"Nome: {i.nome} - Matricula: {i.matricula} - Nota: {i.notas}")


estudante = Estudante("João", 20, 1234)
estudante.adicionandonotas("Matematica", 9.5)

escola = Escola()
escola.adicionar_estudante(estudante)
escola.mostrar_lista()

print()

estudante2 = Estudante("Maria", 19, 1235)
estudante2.adicionandonotas("Hitória", 8.8)

escola2 = Escola()
escola2.adicionar_estudante(estudante2)
escola2.mostrar_lista()