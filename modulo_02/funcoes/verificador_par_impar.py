def verificador():
    eh_par = True
    eh_impar = False
    eh_par_contador = 0
    eh_impar_contador = 0

    while True:
        try:
            num = int(input("Digite um número ou 0 para encerrar: "))
            if num == 0:
                print("Programa encerrado...")
                break
            elif num < 0:
                print("Digite um valor maior que zero.")
            if num % 2 == 0 and num > 0:
                num = eh_par
                eh_par_contador += 1
                print(num)
            elif num % 2 == 1 and num > 0:
                num = eh_impar
                eh_impar_contador += 1
                print(eh_impar)
        except ValueError:
            print("Digite um valor número inteiro válido.")
        
    print(f"Total de números pares: {eh_par_contador}")
    print(f"Total de números impares: {eh_impar_contador}")

verificador()