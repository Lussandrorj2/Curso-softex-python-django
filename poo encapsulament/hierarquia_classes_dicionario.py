class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"Produto: {self.nome} | Preço: {self.preco:.2f}"

class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.marca = marca

    def __str__(self):
        return f"{self.nome} {self.marca} - {self.preco}"

class Roupas(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.nome} {self.tamanho} - {self.preco:.2f}"

class Estoque:
    def __init__(self):
        self.dicionario = {}
    
    def adicionando_produto(self, produto):
        self.dicionario[produto.nome] = produto

    def deletando_produto(self, nome_produto):
        if nome_produto in self.dicionario:
            del self.dicionario[nome_produto]
        else:
            print(f"{nome_produto} não encontrado.")
    
    def lista_produto(self):
        if not self.dicionario:
            print("O estoque está vazio.")
        else:
             for produto in self.dicionario.values():
                 print(produto)

estoque = Estoque()

celular = Eletronico("Smartphone",2800, "iPhone" )
roupa = Roupas("Camisa", 100.00, "G")

estoque.adicionando_produto(celular)
estoque.adicionando_produto(roupa)

estoque.lista_produto()

estoque.deletando_produto("Smartphone")

estoque.lista_produto()

estoque.deletando_produto("Camisa")

estoque.lista_produto()
