lista_a = [1,2,3,4,5,8]
lista_b = [5,6,7,8]
lista_em_comum = []
for lista in (lista_a, lista_b):
    for n in lista:
        if n in lista_a and n in lista_b:
            if n not in lista_em_comum:
                lista_em_comum.append(n)
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
print(f'lista em comum: {lista_em_comum}')