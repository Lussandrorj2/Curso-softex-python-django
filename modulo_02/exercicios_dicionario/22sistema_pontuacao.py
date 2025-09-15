import pyfiglet

print('')
figlet = pyfiglet.figlet_format("<< Brasileirao >>")
print(figlet)
print('')

jogadores = [
{"nome":"Ronaldo", "ponto":10.0},
{"nome":"Rivaldo", "ponto":9.8},
{"nome":"Roberto Carlos", "ponto":9.3},
{"nome":"Ronaldinho Gaucho", "ponto":10.0}
]

for jogador in jogadores:
    print(f'Jogador: {jogador["nome"]} e pontos: {jogador["ponto"]}')

while True:
    novo_jogador = input("Digite o nome de um novo jogador: ")
    if novo_jogador not in jogadores["nome"]:
        jogadores["nome"] = novo_jogador
    else:
        pass
    novo_ponto = int(input("Digite o ponto: "))
    if novo_ponto not in jogadores["ponto"]:
        jogadores["ponto"] = novo_ponto
