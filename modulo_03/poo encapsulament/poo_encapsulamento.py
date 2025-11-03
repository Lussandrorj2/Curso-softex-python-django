class Circulo():
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, novo_raio):
        if isinstance > 0:
            self._raio = novo_raio
        else:
            print("Valor do raio não pode ser negativo.")

    def calcular_area(self):
        area = 3.14*self.raio**2
        print(area)

area = Circulo.calcular_area
print(area)
