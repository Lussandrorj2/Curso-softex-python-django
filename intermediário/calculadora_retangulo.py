class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2* (self.base + self.altura)
    
retangulo = Retangulo(5,3)
area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(f"A area calculada: {area}")
print(f"O perímetro calculado: {perimetro}")