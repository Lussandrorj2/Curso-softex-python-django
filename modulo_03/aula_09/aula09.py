print("Procurando número específico em uma lista")

lista = []
num_especifico = 8
while True:
    num = int(input("Digite um número (ou negatio para sair): "))
    if num < 0:
        break
    lista.append(num)

contador = lista.count(num_especifico)
if contador > 0:
    print(f"O número {num_especifico} foi encontrado {contador} vezes na lista.")
else:
    print(f'O número {num_especifico} não foi encontrado na lista.')

print(f'Número digitados: {lista}')
print("Programa encerrado.")
    