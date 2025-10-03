from classpessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome:str, idade:int, matricula:int):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = {}

    

    def adicionandonotas(self,materia:str, nota:float):
        if materia in self.notas:
            self.notas[materia].append(nota)
        else:
            self.notas[materia] = [nota]

        print(f"Notas de {materia}: {self.notas[materia]}")


    def __str__(self):
        return f"Estudante: {self._nome} - Matricula: {self.matricula}"


# estudante = Estudante("João", 20, 1234)
# estudante.adicionandonotas("Matematica", 9.5)
# print(estudante)

# print()

# estudante2 = Estudante("Maria",19,1235)
# estudante.adicionandonotas("Matemática", 8.7)
# print(estudante2)
        


       

           






       
