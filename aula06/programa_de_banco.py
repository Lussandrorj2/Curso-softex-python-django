"""
data 20/08/2025
Progrma de banco
1- rodar em loop infinito //ok
2- ter conta e senha(validar)
3- encerrar sessão
4- cheque especial (limite saldo negativo)
5- tentar 3x a senha
6- opções(saque,deposito,saldo)
7- mostrar o saldo após o saque
8- alterar senha
9- dizer o nome do usuário
10- pagar boleto

"""
#declaração

conta_corrente = "123456-7"
senha_usuario = "9999"
saldo_atual= 0
limite_saldo_negativo = -500.00
nome_usuario = "José"

while True:
    for i in range(3):
        conta = input("Digite sua conta corrente: ")
        senha = input("Digite sua senha: ")
        if conta == conta_corrente and senha == senha_usuario:
            print(f"Bem-vindo {nome_usuario}!")
            acesso_permitido = True
            break        
        else:
            print("Conta ou senha inválida.")
            acesso_permitido = False
    if not acesso_permitido:
        break
    
    while True:
        opcao = int(input("Escolha uma opção\n"\
        "1- Ver saldo.\n"\
        "2- Sacar valor.\n"\
        "3- Depositar.\n"\
        "4- Pagar boleto.\n"\
        "5- Alterar senha.\n"\
        "6- Sair.\n"))

        if opcao == "1":
            print(f"Seu saldo atual é de {saldo_atual}.")
        elif opcao == "2":
            valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacar <= (saldo_atual + limite_saldo_negativo):
                saldo_atual -= valor_a_sacar
                print("Saldo liberado, retire seu valor.")
            else:
                print("Saldo insuficiente.")
        elif opcao == "3":
            depositar = float(input("Insera o valor a ser depositado: "))
            if depositar > 0:
                saldo += depositar
            else:
                print("Valor inválido.")
        elif opcao == "5":
            pass
        elif opcao == "6":
            print("Atendimento finalizado.")
            break
        else:
            print("opção inválida.")