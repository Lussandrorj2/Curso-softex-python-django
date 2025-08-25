# Declaração
#data25/08/2025
import time
print(" |||||████ LANCHONETE ███||||| ")

hamburguer = 21
cupom = "999"
desconto_cupom = 10
while True:
    produto = input("Digite o nome do produto: ")
    if produto == "hamburguer":
        desconto = input("Digite o número do cupom de desconto: ")
        time.sleep(2)
        print("Pedido confirmado!")
        valor = hamburguer*(1-desconto_cupom/100)
        if desconto == cupom:
            time.sleep(2)
            print(f"O valor do produto com desconto: {valor:.2f}")
            break
        elif desconto != cupom:
            time.sleep(1)
            print(hamburguer)
            break
                                
