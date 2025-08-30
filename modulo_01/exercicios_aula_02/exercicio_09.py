print("=-=-= VERIFICAÇÃO DE IDADE E CNH =-=-=")
print("")

idade = int(input("Digite sua idade: "))
cnh = input("Você tem CNH?(s/n): ").lower()
tem_cnh = cnh == "s"

if idade >= 18 and tem_cnh:
    print("Você pode dirigir.")
elif idade >= 18 and not tem_cnh:
    print("Você não pode dirigir")
else:
    print("Você não pode dirigir.")