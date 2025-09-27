#Encapsulamento e dicionário

class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def get_info(self):
        return {
            'nome':self._nome,
            'idade':self._idade
        }

pessoa1 = Pessoa("Lussandro", 35)
print(pessoa1.get_info())
pessoa2 = Pessoa("Cilene", 34)
print(pessoa2.get_info())
pessoa3 = Pessoa("Julie", 12)
print(pessoa3.get_info())