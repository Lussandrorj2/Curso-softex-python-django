lista = []
soma = 0
while True:
    num = input("Digite um número (ou negarivo para sair): ")
    try:
        num = int(num)
        if num < 0:
            break
        if num <= 100:
            lista.append(num)
            soma += num
    except ValueError:
        pass
        
print(f'Lista de números: {lista}')
print(f'Soma do números: {soma}')
print("progrma encerrado.")