import random

print('╝ Adivinhe um número secreto entre 1 e 100 ╚')
print('')
num = random.randint(1,100)
tentativas = 0
while True:
    try:
        chute = int(input("Digite um palpite entre 1 e 100: "))
        tentativas += 1
        if chute < 1 or chute > 100:
            print("Por favor, digite um número válido entre 1 e 100>")
        elif chute < num:
            print('Muito baixo! Tente novamente.')
        elif chute > num:
            print('Muito alto! Tente novamente.')
        elif chute == num:
            print(f'Parabens! Você acetou o número {num} em {tentativas} tentativas.')
            break
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro.')

