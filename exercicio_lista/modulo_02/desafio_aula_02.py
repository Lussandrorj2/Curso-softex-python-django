print('')
print("Análise de dados de acesso".center(40))
print('')

registros_acesso = []
usuarios_sucesso = set()

while True:
    nome = input("Digite seu nome ou 'parar' para sair: ").strip().upper()
    if nome == "PARAR":
        break

    status = input("Selecionoe o status:\n1) Sucesso\n2) Falha\n Escolha a opção: ")
    if status == "1":
        print("Sucesso")
        status = "Sucesso"
    elif status == "2":
        print("Falha")
        status = "Falha"
    else:
        print("Opção inválida. Digite apenas 1 ou 2")
    try:    
        duracao_minutos = int(input("Digite o tempo de duração: "))
    except ValueError:
        print("Tempo inválido. Digite apenas um número inteiro. Tente novamente.")

    registros_acesso.append((nome,status,duracao_minutos))

    if status == "Sucesso":
        usuarios_sucesso.add(nome)

print("Registros de acesso.: ")
for r in registros_acesso:
    print(r)

print(usuarios_sucesso)

tempo_total_sucesso = 0
for registro in registros_acesso:
    nome = registro[0]
    status = registro[1]
    duracao_minutos = registro[2]
    if status == "Sucesso":
        tempo_total_sucesso += duracao_minutos
print(f"Tempo total de duraçao com sucesso é {tempo_total_sucesso}")





print("Programa encerrado...")