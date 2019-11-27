class Musica:
    def __init__(self, A, B, C, D):
        self.nome = A
        self.artista = B
        self.duracao = C
        self.ano = D

rush1 = Musica('Tom Sawyer', 'Rush', 4.35, 1976)
print('Musica = ', rush1.nome, '\nArtista = ', rush1.artista, '\nDuracao = ', rush1.duracao, '\nAno = ', rush1.ano)
