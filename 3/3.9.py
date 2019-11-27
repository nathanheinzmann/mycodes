class Ponto:
    def __init__(self, A, B):
        self.x = A
        self.y = B

    def graf(self,x,y):
        print('\tx = ',x ,'e y = ', y)


p1 = Ponto(1,3)
p2 = Ponto(2,2)

print('Pontos do grafico:')
print('p1:')
p1.graf(p1.x,p1.y)
print('p2:')
p2.graf(p2.x,p2.y)
