class Musica:
    def __init__(self, artista, titulo):
        self.artista = artista
        self.titulo = titulo

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
    
class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self,musica):
        self.musicas.append(musica)
        
    def tocar_musica(self):
        for musica in self.musicas:
            print(f"Tocando {musica}")


m1 = Musica("Linkin Park", "Numb")

p = Playlist()

p.adicionar_musica(m1)
p.tocar_musica()