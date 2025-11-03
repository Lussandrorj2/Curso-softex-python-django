class Motor:
    def __init__(self):
        pass
    
    def ligar(self):
        print("Motor ligado")

class Roda:
    def __init__(self):
        pass

    def girar(self):
        print("Roda girando")

class Carro:
    def __init__(self):
        self.motor = Motor()
        self.rodas = [Roda() for _ in range(4)]
        
    def ligar_carro(self):
        self.motor.ligar()
        for roda in self.rodas:
            roda.girar()

meu_carro = Carro()
meu_carro.ligar_carro()