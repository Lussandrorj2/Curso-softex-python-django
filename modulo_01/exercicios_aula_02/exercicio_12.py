soma = 0
contador = 1

while contador <=5:
    num = int(input(f'Digite o {contador}º número: '))
    soma += num
    contador += 1
print(f'A soma dos números é {soma}')