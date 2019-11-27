class LampadaTresEstados:
    def estado(self, x):
        self.estado = x
        if x == 100:
            print('Acesa.')
        elif x == 0:
            print('Apagada.')
        else:
            print('Meia-Luz.')
    def estaLigada(self):
        if self.estado == 0:
            return False
        elif self.estado == 100:
            return True

lampada = LampadaTresEstados()
lampada.estado(int(input('Luminosidade: ')))
print(lampada.estaLigada())