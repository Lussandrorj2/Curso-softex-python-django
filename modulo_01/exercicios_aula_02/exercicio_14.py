print('=^=^= Soma de números positivos =^=^=')
print('')

contador = 0
while True:
    num = int(input("Digite um número (ou negativo para sair): "))
    if num < 0:
        break
    contador += num

print(f'A soma dos números positivos é {contador}')
                    