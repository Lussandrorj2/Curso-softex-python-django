numeros = [10, 5, 20, 15]

if len(numeros) < 2: # Verifica se a lista tem pelo menos 2 elementos
    print("A lista deve ter pelo menos 2 elementos.")
else:

    if numeros[0] > numeros[1]:
        maior = numeros[0]
        segundo_maior = numeros[1]
    else:
        maior = numeros[1]
        segundo_maior = numeros[0]
    for num in numeros[2:]: # Inicia o loop a partir 3 item
        if num > maior:
            segundo_maior = maior
            maior = num
        elif num > segundo_maior:
            segundo_maior = num
print(segundo_maior)