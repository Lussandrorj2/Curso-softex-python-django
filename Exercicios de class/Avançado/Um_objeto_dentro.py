class Motor():
    def __init__(self, potencia):
        self.potencia = potencia

class Carro():
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        print(f"A potencia do motor é {self.motor.potencia}")

carro1 = Carro("Fusca", 100)
carro1.exibir_potencia()