class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
    
class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            return f"A música {musica} foi removida com sucesso."
        else:
            return f"A música não está na playlist."
        
    def tocar_playlist(self):
        for musica in self.musicas:
            print(f"Está tocando {musica.titulo} de {musica.artista}")

m1 = Musica("Só os loucos sabem", "Charlie Brown Jr.")
m2 = Musica("Numb", "Link Park")
m3 = Musica("Sonhos", "MC Marcinho")

minha_play = Playlist()

minha_play.adicionar_musica(m1)
minha_play.adicionar_musica(m2)

print(m1) 
print(m2)

minha_play.tocar_playlist()

print()

#minha_play.remover_musica(m1)

print(minha_play.remover_musica(m1))    
minha_play.adicionar_musica(m3)


minha_play.tocar_playlist()