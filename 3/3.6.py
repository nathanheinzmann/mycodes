class SerieA:
    def __init__(self, A, B, C, D, E, F):
        self.time = A
        self.pontos = B
        self.vitorias = C
        self.derrotas = D
        self.empates = E
        self.saldogol = F


Santos = SerieA('Santos', 17, 4, 1, 5, 8)

print('Time = ', Santos.time, '\nPontos = ', Santos.pontos)