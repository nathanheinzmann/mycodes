
class animal():
    def __init__(self, n, r):
        self.nome=n
        self.raca=r

    def caminha(self):
        print("caminhando")
 
class cachorro(animal):
    def __init__(self, n, r):
        super().__init__(n,r)
    def exibeDados(self):
        print("nome = ", self.nome, ", raça = ", self.raca)
    def late(self):
        print("au au")
        
class gato(animal):
    def __init__(self, n, r):
        super().__init__(n,r)
    def exibeDados(self):
        print("nome = ", self.nome, ", raça = ", self.raca)
    def mia(self):
        print("miauu")

a1 = cachorro("Tobi", "Vira-Lata")
a1.exibeDados()
a1.late()
a1.caminha()

a2 = gato("Gatito", "Siames")
a2.exibeDados()
a2.mia()
a2.caminha()
