class carro():
    def __init__(self, v):
        self.velocidade=v
    def liga(self):
        print ("carro liga")

class barco():
    def __init__(self, v):
        self.velocidade=v
    def liga(self):
        print ("barco liga")  

class carroanfibio2(barco, carro):
    def __init__(self, v):
        super().__init__(v)


c=carroanfibio2(10)
c.liga()
        