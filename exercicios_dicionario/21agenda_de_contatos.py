agenda = dict()

while True:
    print(" Menu:\n 1) Adicionar contato\n 2) Buscar contao\n 3) Sair\n")

    adicionar_contato = input("Digite o nome do contato ou 'parar' para sair: ").strip().lower()
    if adicionar_contato == "parar":
        print("Programa encerrado...")
        break
    adicionar_numero = input("Digite o número de telefone: ").strip()

    if adicionar_contato not in agenda:
        agenda[adicionar_contato] = adicionar_numero

    