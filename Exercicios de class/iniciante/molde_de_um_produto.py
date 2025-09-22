class Produto():
    def __init__(self, nome=str, preço=float):
        self.nome = nome
        self.preço = preço
    
    def __str__(self):
        return f"O {self.nome} custa R$ {self.preço:.2f}"
    
    
caderno = Produto("Caderno", 15.50)
caneta= Produto("Caneta", 3.00)
print(caderno)
print(caneta)