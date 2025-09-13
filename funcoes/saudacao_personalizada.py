def saudacao():
    while True:
        nome = input("Digite seu nome ou 0 para sair: ")
        if nome == "0":
            print("Programa encerrado...")
            break

def idade():
    maior = 0
    menor = 0
    lista_maior = []
    lista_menor = []
    while True:
        nome = input('Digite seu nome ou 0 para encerar: ')
        if nome == "0":
            print("Programa encerrado...")
            break
        
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            maior +=1
            lista_maior.append(nome)
            print(f"Você está com {idade} e já é maior de idade")
        else:
            menor += 1
            lista_menor.append(nome)
            print(f"Você está com {idade} e é menor de idade.")
    print(f"Tem {maior} maiores de idade.")
    print(f" As pessoas maiores de idade são: {', '.join(lista_maior)}")
    print(f"Tem {menor} menores de idade.")
    print(f"As pessoas menores de idade são: {', '.join(lista_menor)}")

print(idade())
