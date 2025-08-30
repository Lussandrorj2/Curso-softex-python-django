saldo = 1000.00
while True:
    print('\n---Caixa Eletrônico---')
    print('1- Sacar\n2- Depositar\n3- Ver Saldo\n4- Sair')
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        saque = float(input('Digite o valor para saque: '))
        if saque > saldo:
            print('Saldo insuficiente para saque.')
        else:
            saldo -= saque
            print(f'Saque de R${saque:.2f} realizado com sucesso.')
    elif opcao == 2:
        deposito = float(input('Digite o valor para depósito: '))
        saldo += deposito
        print(f'Depósito de R$ {deposito:.2f} realizado com sucesso>')
    elif opcao == 3:
        print(f'Seu saldo atual é R$ {saldo:.2f}')
    elif opcao == 4:
        print('Serviço encerrodo. Volte sempre!')
        break
    else:
        print('Opção inválida. Tente novamente.')