print("\033[34m█ █ █ █ MENU DE COMANDOS PARA UM ROBÔ █ █ █ █\033[m")

posicao = 0
robo = 0
menu = ""
while True:
    menu = input("Escolha uma opção:\n" \
    "1 - Avançar\n" \
    "2 - Recuar\n" \
    "3 - Status\n" \
    "4 - Desligar\n")

    if menu == "1":
        posicao += robo
        print(f"O robô avança {posicao+1} posição")
    elif menu == "2":
        posicao -= robo
        print(f"O robo recua {posicao-1} posição.")
    elif menu == "3":
        posicao == robo
        print(f"O robo está no {posicao} Status")
    if menu == "4":
        print("Programa encerrado.")
        break