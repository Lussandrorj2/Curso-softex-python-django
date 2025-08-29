print(">>>> Programa de notas escolares com Loop While <<<<\n")

while True:  # loop principal para múltiplos alunos
    notas = []
    soma_notas = 0

    # Entrada de dados do aluno
    nome = input("Digite o nome do aluno: ").strip()
    matricula = input("Digite a matrícula do aluno: ").strip()

    if not nome or not matricula:
        print("Nome e matrícula não podem estar vazios. Insira os valores corretamente.\n")
        continue  # volta ao início do loop principal

    # Loop para inserir notas
    while True:
        try:
            nota = float(input("Insira a nota (ou -1 para encerrar o cadastro deste aluno): "))

            if nota == -1:
                break  # sai do loop de notas

            if 0 <= nota <= 10:
                notas.append(nota)
                soma_notas += nota
            else:
                print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")

        except ValueError:
            print("Valor inválido. Por favor, insira apenas números.")

    # Processamento final do aluno
    if notas:
        media = soma_notas / len(notas)
        print("\n\033[36m==== Boletim Escolar ====\033[m")
        print(f"Aluno: {nome}")
        print(f"Matrícula: {matricula}")
        print(f"A média das notas é: {media:.2f}")
        print(f"As notas inseridas foram: {notas}")

        if media >= 9:
            print(f"\033[34mExcelente! Você está aprovado com louvor {nome}!\033[m")
        elif 7 <= media < 9:
            print(f"\033[32mParabéns! Você está aprovado {nome}!\033[m")
        elif 5 <= media < 7:
            print(f"\033[33mVocê está de recuperação {nome}.\033[m")
        else:
            print(f"\033[31mInfelizmente, você está reprovado {nome}.\033[m")
    else:
        print("Nenhuma nota foi inserida.")

    # Pergunta se deseja cadastrar outro aluno
    continua = input("\nDeseja cadastrar outro aluno? (S/N): ").strip().upper()
    if continua != 'S':  # se não digitar 'S', sai do loop principal
        print("Encerrando o programa...")
        break  # agora o break está dentro do loop principal

# Mantém a janela aberta
input("\nPressione ENTER para sair do programa...")
