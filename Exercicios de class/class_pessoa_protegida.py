class Pessoa():
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome   
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, (str)):
            self._nome = novo_nome
        else:
            print("Erro! ")
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade,(int)) and nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("Erro! Número não é inteiro ou positivo.")




pessoa1 = Pessoa("João", 36)
print(pessoa1.nome)
pessoa1.nome="Zé"
print(pessoa1.nome)
pessoa1.nome="Juliana"
print(pessoa1.nome)
print(pessoa1.idade)
pessoa1.idade = 30
print(pessoa1.idade)
pessoa1.idade = 22
print(pessoa1.idade)
pessoa1.nome = "Alexandre"
pessoa1.idade = 33
print(pessoa1.nome)
print(pessoa1.idade)