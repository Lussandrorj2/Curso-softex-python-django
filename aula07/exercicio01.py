# Declaração
#data25/08/2025
import time
print("\033[45m |||||████ LANCHONETE ███||||| \033[m")

hamburguer = 21.90
cupom = "999"
desconto_cupom = 10
while True:
    produto = input("Digite o nome do produto: ")
    if produto == "hamburguer":
        desconto = input("Digite o número do cupom de desconto: ")
        time.sleep(2)
        print("\033[032mPedido confirmado!\033[m")
        valor = hamburguer*(1-desconto_cupom/100)
        if desconto == cupom:
            time.sleep(2)
            print(f"\033[034mO valor do produto com desconto: R$ {valor:.2f}\033[m")
            break
        elif desconto != cupom:
            time.sleep(1)
            print(f"\033[34mR$ {hamburguer}\033[m")
            break
                                
