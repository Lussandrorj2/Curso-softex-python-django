import pyfiglet

print(pyfiglet.figlet_format("AGENDA"))

agenda = dict()

while True:
        operacao = input(" Menu:\n 1) Adicionar contato\n 2) Buscar contao\n 3) Sair\n")

        if operacao == "1":
            nome = input("Digite o nome do contato: ")
            num = input("Digite o número do contato: ")
            agenda[nome] = num
            print(f"Contato {nome} adicionado com sucesso.")
        elif operacao == "2":
            buscar = input("Digite o nome ou número do contato: ")
            encontrado = False
            for nome, num in agenda.items():
                if buscar == nome or buscar == num:
                    print(f"{nome} → {num}")
        elif operacao == "3":
            print("Operação encerrada.")
            break
        else:
            print("Contato não encontrado.")
  

    