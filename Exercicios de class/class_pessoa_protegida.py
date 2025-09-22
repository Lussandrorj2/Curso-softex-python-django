class Pessoa():
    def __init__(self, nome:str, idade:int):
        if nome and isinstance(nome, int):
            self._nome = nome
        else:
            self._nome = "Nome desconhecido"
        if idade > 0 and isinstance(idade, int):    
            self._idade = idade
        else:
            self._idade = "Idade desconhecida"    

    @property #DEVOLVE O VALOR ATRIBUIDO PROTEGIDO
    def nome(self):
        return self._nome   
    
    @nome.setter # ALTERA O VALOR ATRIBUIDO PROTEGIDO
    def nome(self, novo_nome:str):
        if isinstance(novo_nome, (str)) and novo_nome:
            self._nome = novo_nome
        else:
            print("Erro! O novo nome deve ser uma string e não vazia.")
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade:int):
        if isinstance(nova_idade,(int)) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Erro! Número deve ser inteiro e positivo.")




pessoa1 = Pessoa("", -1)
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