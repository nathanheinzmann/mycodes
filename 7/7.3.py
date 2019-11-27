class carro():
    def __init__(self, v):
        self.velocidade=v
    def liga1(self):
        print ("carro liga")

class barco():
    def __init__(self, v):
        self.velocidade=v
    def liga2(self):
        print ("barco liga")  

class carroanfibio(carro,barco):
    def __init__(self, v):
        super().__init__(v)


c=carroanfibio(10)
c.liga1()
        