lista = [5,6,9,7,4,1,6,8,9,6]
numero_procurado = 6
contador = 0

for numero in lista:
    if numero == numero_procurado:
        contador += 1
print(f'O número é {numero_procurado}\n O numero procurado aparece {contador}\n A lista é {lista}')