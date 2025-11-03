class Motor:
    def ligar_motor(self):
        print("O motor ligou.")

class Carro:
    def __init__(self):
        self.Motor = Motor()

    def ligar(self):
        print("O carro está ligando.")
        self.Motor.ligar_motor()

carro = Carro()

carro.ligar()

print(carro)
