print("=== COMPARANDO NÚMEROS ===")
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))

if num_1 > num_2:
    print(f"{num_1} é maior que {num_2}.")
elif num_1 < num_2:
    print(f"{num_2} é maior que {num_1}.")
else:
    print("Os números são iguais!")