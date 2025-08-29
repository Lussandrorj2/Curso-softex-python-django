print("\033[33m █ █ █ TABUADA █ █ █ \033[m")
num = int(input("Digite um número: "))
for i in range(1,11):
    resultado = num * i
    print(f"\033[34m{num} X {i} = {resultado} \033[m")