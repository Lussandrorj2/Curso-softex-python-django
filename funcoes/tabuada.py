import pyfiglet

print(pyfiglet.figlet_format("TABUADA"))

def tabuada(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

while True:
    num = int(input("Digite um número ou 0 para sair: "))
    if num <= 0:
        print(pyfiglet.figlet_format("Programa encerrado..."))
        break
    tabuada(num)