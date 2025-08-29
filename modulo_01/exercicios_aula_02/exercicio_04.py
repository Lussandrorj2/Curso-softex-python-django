print(" █ █ █ Validação de senha █ █ █ ")
senha_secret = "123abc"
senha = input("Digite a senha: ")
if senha_secret == senha:
    print("Acesso liberado!")
else:
    print("Senha incorreta.")