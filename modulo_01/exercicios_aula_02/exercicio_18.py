num = int(input('Digite um número para calcular o fatorial: '))
if num < 0:
    print('Numeros negativos não possuel fatorial')
else:
    fatorial = 1
    i = 1
    while i <= num:
        fatorial = fatorial * i
        i += 1
    print(f'O fatorial de {num} é {fatorial}')
