produtos = {"capa iphone 12":10, "Capa iphone 13":15, "capa iphone 14":20}
estoque = {}

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

print("\nEstoque final")
for produto, qdt in estoque.items():
   print(f"{produto} → {qdt} unidade(s)")
print(f"Estoque atualizado total → {produtos[produto]}")