class LampadaTresEstados:
    def estado(self, x):
        if x == 100:
            print('Acesa.')
        elif x == 0:
            print('Apagada.')
        else:
            print('Meia-Luz.')

lampada = LampadaTresEstados()
lampada.estado(int(input('Luminosidade: ')))