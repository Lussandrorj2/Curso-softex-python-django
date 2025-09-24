class Midia():
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Título: {self.titulo} | Duração: {self.duracao_seg}")

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Titulo: {self.titulo} | Duração: {self.duracao_seg} | Artista: {self.artista}")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Título: {self.titulo} | Duração: {self.duracao_seg} | Resolução: {self.resolucao}")

musica = Musica("One last berath",03.57, "Creed")
video = Video("Numb", 3.50, "1080x900")

dic_play = {"musicas":[],"videos":[]}
