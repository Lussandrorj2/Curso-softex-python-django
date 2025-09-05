estoque_principal = [("camisa",101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]

set_principal = set(estoque_principal)
set_online = set(estoque_online)
print('')
estoque_total = set_principal.union(set_online)
print(f"Estoque total: {estoque_total}")
print('')
nos_dois = set_principal.intersection(set_online)
print(f"Produtos disponíveis na loja e no site são: {nos_dois}")
print('')
apenas_loja = set_principal.difference(set_online)
print(f"Produtos disponíveis apenas na loja: {apenas_loja}")
print('')
apenas_online = set_online.difference(set_principal)
print(f"Produtos disponíveis online: {apenas_online}")