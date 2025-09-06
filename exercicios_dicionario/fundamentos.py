#frutas = {"Maçã", "Melancia", "Mamão"}
'''frutas = dict(maçã=5, morango=10, banana=15)
print(frutas)
print(f'O valor do morango é R$ {frutas['morango']:.2f}'.replace('.',','))
print(f'O valor da banana é R$ {frutas['banana']:.2f}'.replace('.',','))'''

vazio = dict()
contador = 0

while True:
     try:
        valor = int(input('Digite um valor para ser adicionado ao dicionário ou negativo para sair: '))
     except ValueError:
         print("Erro! Digite somente números inteiros.")
         continue
     
     if valor < 0:
         print("Programa encerrado")
         break
     
     vazio[f'Dicionário{contador}'] = valor
     contador += 1

print(f"Dicionário final → {vazio}")
     