from random import randint
from estatisticas import calcular_media as media_1

notas = [randint(0, 100) for _ in range(10)]
print(f"Notas geradas: {notas}")

media = media_1(notas)
print(f"A média das notas é {media:.2f}")
