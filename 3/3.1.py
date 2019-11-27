class produto:
    def __init__(self, A, B, C):
        self.valor = A
        self.potencia = B
        self.tipo = C

lampada = produto(9.99, "10W", "LED")

print(lampada.tipo)