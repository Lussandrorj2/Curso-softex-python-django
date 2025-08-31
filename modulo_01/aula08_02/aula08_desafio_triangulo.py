#Declaração
print(" ▲ ▲ ▲ DESAFIO DO TRIÂNGULO ▲ ▲ ▲ ")
print(" ▲ ".center(32))
print(" ▲▲▲▲ ".center(32))
print(" ▲▲▲▲▲▲▲▲▲▲ ".center(32))
print(" ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ ".center(32))
print(" ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ ".center(32))
print("")
lados = []
while len(lados) < 3:
    try:
        lado = int(input(f"\033[034mDigite o {len(lados)+1}º lado do triângulo: \033[m"))
        if lado > 0:
            lados.append(lado)
        else:
            print("Digite um número positivo e maior que zero.")
    except ValueError:
        print("Error: Digite um número inteiro.")
   
lado_a, lado_b, lado_c = lados

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    if (lado_a > abs(lado_b - lado_c)) and (lado_b > abs(lado_a - lado_c)) and (lado_c > abs(lado_a - lado_b)):
        if lado_a == lado_b and lado_b == lado_c:
            print("Pode ser um triângulo equilátero.")
            print(f"Lados dos triângulo {lados}")
        elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
            print("Pode ser um triângulo isósceles..")
            print(f"Lados do triângulo {lados}.")
        else:
            print("Pode ser um escaleno.")
            print(f"Lados do triângulo {lados}")
    else:
        print("Não pode ser um triângulo devido a diferença de lados.")
else:
    print("Não pode ser um triângulo devido a soma de lados.")

