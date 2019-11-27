class LampadaTresEstados:
    def liga(self):
        print('Acesa')
    def desliga(self):
        print('Apagada')
    def meia(self):
        print('Meia-Luz')

estado = LampadaTresEstados()

estado.liga()
estado.desliga()
estado.meia()