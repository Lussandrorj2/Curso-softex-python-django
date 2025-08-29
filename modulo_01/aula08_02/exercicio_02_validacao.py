print(" ▀ ▀ ▀ ▓ ▓ ▓  VALIDAÇÃO E FORMATAÇÃO DE TELEFONE ▓ ▓ ▓ ▀ ▀ ▀ ")
valido = True
telefone = input("Digite um número de telefone: ")
for c in telefone:
    contador_repetidos = 0
    for n in telefone:
        if c == n:
            contador_repetidos += 1
        if contador_repetidos >=3:
            print("Não pode ter três números repetidos.")
            valido = False
            break
if len(telefone) <= 10:
    print("Necessário que o número de telefone tenha 11 números.")
elif len(telefone) >= 12:
    print("Necessário que o número de telefone tenha 11 números.")
elif not telefone.isdigit():
    print("Necessário que tenho somente números.") 
else:
    print(f"Número {telefone} cadastrado com sucesso!")

