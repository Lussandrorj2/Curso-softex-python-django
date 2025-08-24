print(">>>> Programa de notas escolares com Loop While <<<<")

# declaração
notas = []
soma_notas = 0 # variável para armazenar a soma das notas
nome = ""
matricula = ""

nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
if not nome and not matricula:
    print("Nome e matrícula não podem estar vazios. Insira os valores corretamente.")

while True:
    try: # tratamento de erro para entradas inválidas.
        nota = float(input("Insira a nota (ou -1 para sair): "))

        if nota == -1: # condição de saída do loop.
            break

        if 0 <= nota <= 10: # validação da nota com cade
            notas.append(nota) # adiciona a nota à lista.
            soma_notas += nota # soma as notas.
        else:
            print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        
    except ValueError: # tratamento de erro para entradas inválidas.
        print("Valor inválido. Por favor, insira uma nota entre 0 e 10.")

if notas: # verifica se a lista de notas não está vazia.
    media = soma_notas / len(notas) # cálculo da média.
    print(f"A média das notas é: {media:.2f}")
    print(f"As notas inseridas foram: {notas}")

    if media >= 9:
            print(f"\033[34mExcelente! Você está aprovado com louvor {nome}!\033[m")
    elif 7 <= media < 9:
        print(f"\033[32mParabéns! Você está aprovado {nome}!\033[m")
    elif 5 <= media < 7:
        print(f"\033[33mVocê está de recuperação {nome}.\033[m")
    elif 0 <= media < 5:
        print(f"\033[31mInfelizmente, você está reprovado{nome}.\033[m")