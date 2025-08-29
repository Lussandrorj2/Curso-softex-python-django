print(">>>>> PRODUTO COM DESCONTO <<<<")
preco = float(input("Digite o preço do produto: "))
if preco > 100:
    desconto = preco * 0.1
    novo_preco = preco - desconto
    print(f"O preço do produto com desconto de 10% é R$ \033[31m{novo_preco}\033[m")
else:
    print(f"O preço do produto é R$ \033[32m{preco}\033[m")