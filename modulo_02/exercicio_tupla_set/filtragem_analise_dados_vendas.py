lista_vendas = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1), ("Fone", 45, 1), ("Webcam", 75.20, 2)]

vendas_filtrada = [] # Tupla criada vazia
produtos_unicos = set() # Conjunto criado vazio, conjunto não repete valores repetidos.
for nome, valor, quat in lista_vendas:
    if valor * quat >= 100:
        vendas_filtrada.append((nome,valor,quat))
    produtos_unicos.add(nome)
print('')
print(f'Vendas filtradas:\n {vendas_filtrada}')
print('')
print(f'Produtos únicos:\n {produtos_unicos}')

