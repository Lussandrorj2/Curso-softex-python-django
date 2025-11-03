lista_a = ['verde', 'vermelho', 'rosa', 'azul']
lista_b = ['azul', 'preto', 'rosa', 'amarelo']
lista_em_comum = []
for lista in lista_a, lista_b:
    for n in lista:
        if n in lista_a and n in lista_b:
            if n not in lista_em_comum:
                lista_em_comum.append(n)
print(f'lista A: {lista_a}\nlista B: {lista_b}')
print(f'Lista em comum: {lista_em_comum}')
print("programa encerrado.")