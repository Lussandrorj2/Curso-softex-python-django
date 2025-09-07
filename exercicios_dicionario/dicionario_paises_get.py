paises = {"Brasil":"Brasília", 
          "Paraguai":"Assunção", 
          "Argentina":"Buenos Aires", 
          "Equador":"Quito", 
          "Colômbia":"Bogóta", 
          "Venezuela":"Caracas", 
          "Chile":"Santiago", 
          "Peru":"Lima", 
          "Uruguai":"Montevidéu", 
          "Guiana":"Georgetown", 
          "Suriname":"Paramaribo", 
          "Guiana Francesa":"Caiena"}
while True:
    nome = input("\033[33mDigite o nome de um país da américa do sul: \033[m").strip().title()
    if nome == "parar":
        print("Programa encerrado...")
        break

    capital = paises.get(nome)
    if capital:
        print(f"\033[32mA capital do {nome} é {capital}\033[m")
    else:
        print("País fora da américa do sul. Tente novamente.")