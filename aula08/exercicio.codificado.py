#declaração
frase = input("Digite uma frase: ")

codificada = frase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
decodificada = frase.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")

print(f"Frase codificada → {codificada} \ " ,f"Frase decodificada {decodificada}")