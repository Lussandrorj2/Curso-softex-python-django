print("¦ ¦ ¦ jogo de adivinhar o número ¦ ¦ ¦")

num_secreto = 6

for i in range(5):
    tentativa = int(input("Adivinhe um número de 0 a 10: "))
    if tentativa == num_secreto:
        print("Parabéns! Você acertou!!!")
    elif 0 <= tentativa <= 3:
        print("Está frio!!!")
    elif tentativa == 4 or tentativa == 5:
        print("Está quente!!!")
    elif tentativa == 7 or tentativa == 8:
        print("Está quente!!!")
    elif tentativa >=9:
        print("Está frio!!!")
    else:
        print("Número inválido.")
print("Game over!!!")