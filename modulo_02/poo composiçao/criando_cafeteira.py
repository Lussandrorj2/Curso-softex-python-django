class GraoDeCafe:
    def __init__(self):
        pass
    
    def moer(self):
        print("Os grãos de café foram moídos")

class Agua:
    def __init__(self):
        pass

    def aquecer(self):
        print("A água está aquecida.")

class Cafeteira:
    def __init__(self):
        self.GraoDeCafe = GraoDeCafe()
        self.Agua = Agua()

    def preparar_cafe(self):
        self.GraoDeCafe.moer()
        self.Agua.aquecer()

cafeteira = Cafeteira()

cafeteira.preparar_cafe()

print(cafeteira)