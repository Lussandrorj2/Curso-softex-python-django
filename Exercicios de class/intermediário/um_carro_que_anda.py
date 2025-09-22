class Carro():
    def __init__(self, modelo, nivel_combustivel):
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel  # Combustível disponível
        self.distancia_percorrida = 0  # Distância inicial

    def abastecer(self, litros):
        if litros > 0:
            self.nivel_combustivel += litros
            print(f"Carro abastecido com {litros} litros.")
        else:
            print("Quantidade de combustível inválida para abastecimento.")

    def dirigir(self, distancia):
        consumo_por_km = 0.1  # 0.1 litro por km, ou 1 litro a cada 10 km
        combustivel_necessario = distancia * consumo_por_km  # Combustível necessário para percorrer a distância
        
        if self.nivel_combustivel >= combustivel_necessario:
            self.nivel_combustivel -= combustivel_necessario  # Subtrai o combustível usado
            self.distancia_percorrida += distancia  # Atualiza a distância percorrida
            print(f"O carro percorreu {distancia} km.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

carro = Carro("Fusca", 50)
print(f"Modelo: {carro.modelo}")
carro.abastecer(10)
carro.dirigir(40)
print(f"Combustivel restante {carro.nivel_combustivel} L.")