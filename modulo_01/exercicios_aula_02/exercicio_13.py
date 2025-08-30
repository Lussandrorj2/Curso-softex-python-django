print("╝ Verificação de senha com while ╚")
print("")
senha_correta = "123"
tentativas = 0
while tentativas <= 3:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("\033[32mAcesso permitido.\033[m")
        break
    else:
        print(" Senha incorreta! Tente novamente.")
        tentativas += 1
    if tentativas == 3:
        print("\033[31mAtenção!\033[m \033[33mnúmero máximo de tentativas atingido.\033[m \033[31mAcesso bloqueado!\033[m")
        break