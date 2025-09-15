import pyfiglet

print(pyfiglet.figlet_format("|| Analisador de Frases ||"))

def frase():
    while True:
        frase = input("Digite uma frase ou 0 para sair: ")
        if frase == "0":
            print("Programa encerrado...")
            break
     
        vogais = "aeiouAEIOUáéíóúÁÉÍÓÚ"

        qdt_palavras = len(frase.split())
        qdt_vogais = sum(1 for letra in frase if letra in vogais)
        qdt_consoantes = sum(1 for letra in frase if letra.isalpha() and letra not in vogais)

        frase_palindromo = "".join(letra.lower() for letra in frase if letra.isalpha())
        eh_palindromo = frase_palindromo == frase_palindromo [::-1]

        print(f"Frase → {frase}")
        print(f"Palavras: {qdt_palavras}")
        print(f"Vogais: {qdt_vogais}")
        print(f"Consoantes: {qdt_consoantes}")
        print(f"É palíndromo {'Sim' if eh_palindromo else 'Não'}\n")

frase()