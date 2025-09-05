acessos = [("Pedro", "Sucesso"), ("Ana", "Falha"), ("Maria", "Sucesso"), ("Pedro", "Falha"), ("Ana", "Falha")]

sucesso = set()
falha = set()

for nome, login in acessos:
    if login == "Sucesso":
        sucesso.add(nome)
    elif login == "Falha":
        falha.add(nome)
falha = falha.difference(sucesso)

print(f'Usuário com pelo menos um login com sucesso: {sucesso}')
print(f'Usuário que tiveram somente falha no login: {falha}')
