print("### Programa de notas escolares com loop for ###")
#add data: 21/08/2023
#declaração
notas = [] # lista para armazenar as notas
soma_notas = 0 # variável para armazenar a soma das notas
try:# tratamento de erro para entradas inválidas
    quantidade_notas = int(input("Quantas notas você deseja inserir? "))
    soma = 0 # variável para armazenar a soma das notas
except ValueError: # tratamento de erro para entradas inválidas
    print("Valor inválido. Por favor, insira um númuero vádlido.")
    quantidade_notas = int(input("Quantas notas você deseja inserir? "))
for i in range(quantidade_notas):
    try: # loop para inserir as notas
        nota = float(input(f"Digite a nota {i + 1}ª: "))
        if 0 <= nota <= 10: # validação da nota com cadeamento
            notas.append(nota) # adiciona a nota à lista
            soma_notas += nota # soma as notas
        else:
            print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
    except ValueError: # tratamento de erro para entradas inválidas
        print("Valor inválido. Por favor, insira uma nota entre 0 e 10.")
media = soma_notas / len(notas) # cálculo da média
if 0 < nota <= 10: # validação da média com cadeamento
    print(f"A média das notas é: {media:.2f}")
    print(f"As notas inseridas foram: {notas}")
if media >= 9:
    print("\033[34mExcelente! Você está aprovado com louvor!\033[m")
elif 7 <= media < 9:
    print("\033[32mParabéns! Você está aprovado!\033[m")
elif 5 <= media < 7:
    print("\033[33mVocê está de recuperação.\033[m")  
else:
    print("\033[31mInfelizmente, você está reprovado.\033[m")