produtos = {"capa iphone 12":10, "capa iphone 13":15, "capa iphone 14":20}
estoque = {}
print(f"Capa iPhone 12\n"
      "Capa iPhone 13\n"
      "Capa iPhone 14\n")

while True:
   produto = input("Digite o nome do produto ou 'parar' para sair: ").strip().lower()
   if produto == "parar":
      print("programa encerrado...")
      break
   if produto not in produtos:
      print("Produto não encontrado. Tente novamente.")
      continue
   try:
      quantidade = int(input("Digite a quantidade de produtos: "))
   except ValueError:
      print("Quandtidade inválida. Digite um número maior que zero.")
      continue
   
   if quantidade > 0:
      estoque[produto] = estoque.get(produto,0) + quantidade
      print(f"{quantidade} unidade(s) de {produto} adicionada(s) ao estoque.")
   else:
      print("Quantidade inválida. Adicione uma quantidade maior que zero.")

print("\nEstoque final de capa item")
for produto, qdt in estoque.items():
   estoque_total = qdt + estoque.get(produto,0)
   print(f'{produto} atualizado para {estoque_total} unidade(s).')

print("Estoque total de todos os itens atualizado")
estoque_final = 0
for p, v in produtos.items():
   estoque_inicial = estoque.get(p,0)
   estoque_final += v + estoque_inicial
print(f'Estoque total dos produtos → {estoque_final}')
 