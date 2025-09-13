def media():
    notas = []
    while True:
        qtd_nota = int(input("Informe a quantidade de notas que irá lançar: "))
        for i in range(qtd_nota):
            nota = float(input(f"Digite a {i+1}º nota: "))
            notas.append(nota)

        media = sum(notas) / len(notas)    
    
        if media >= 8:
            print("Parabéns! Passou com louvor!")
        elif media >= 7:
            print("Parabéns! Você está aprovado.")
        elif media >= 6:
            print("Você está em recuperação!")
        else:
            print("Você está reprovado.")
        
        print(f"A média é {media:.2f}")
        
        c = input("Deseja continuar: (s/n): ").strip().lower()
        if c == "n":
            print("Programa encerrado.")
            break

media()