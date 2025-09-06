pares = ((2,2),(3,3),(4,4)) #Tuplas

soma = sum([sum(par) for par in pares]) #Utilizando list comprehension

print(f'A soma feita do jeito mais breve é {soma}')

soma = 0 

for par in pares: #Loop for padrão
    soma += sum(par)

print(f'A soma feita do jeito mais longo é {soma}')