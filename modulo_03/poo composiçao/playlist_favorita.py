class Musica:
    def __init__(self, artista, titulo):
        self.artista = artista
        self.titulo = titulo

    def __str__(self):
        return f"{self.titulo} | {self.artista}"
    
class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"A música {musica} foi removida com sucesso.")
        else:
            print("Música não encontrada.")
    
    def tocar(self):
        print("Tocando playlist")
        for musica in self.musicas:
            print(f'- {musica}')

class Fav(Playlist):
    def tocar(self):
        print("<<<Tocando playlist favorita>>>")
        for m in self.musicas:
            print(f"Tocando da playlist favorita - {m}")

m1 = Musica("Numb", "Link Park")
m2 = Musica("Sonho", "Mc Marcinho")
m3 = Musica("Te amo demais", "Mc Marcinho")
m4 = Musica("Zói de lula", "Charlie Brown Jr.")

play = Playlist()
play.adicionar_musica(m1)
play.adicionar_musica(m2)
play.adicionar_musica(m3)
play.adicionar_musica(m4)

play.tocar()
print()

fa = Fav()
fa.adicionar_musica(m1)
fa.adicionar_musica(m4)
fa.tocar()