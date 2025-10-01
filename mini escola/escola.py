from classestudante import Estudante

class Escola:
    def __init__(self):
        self.lista_estudante = []

    def adicionar_estudante(self, estudante):
        self.lista_estudante.append(estudante)

    def mostrar_lista(self):
        for i in self.lista_estudante:
            print(f"Nome: {i.nome} - Matricula: {i.matricula} - Nota: {i.nota}")

escola = Escola()
escola.mostrar_lista()