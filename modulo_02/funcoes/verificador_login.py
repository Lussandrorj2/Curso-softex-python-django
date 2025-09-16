
def verificador():
    tentativas = 0
    while tentativas < 3:
        try:
            login = input("Digite seu login: ").strip()
            senha = input("Digite sua senha: ")

            if login == "admin" and senha == "1234":
                verificador = True
                print("Acesso concedido")
                return
            else:
                tentativas += 1
                print(f"Acesso negado. Login ou senha incorretos. Você já tentou {tentativas} de 03")
        except ValueError:
            print("Erro! Digite novamente.")      
    print("Conta bloqueada. Entre em contato com a administração.")               
        
verificador()