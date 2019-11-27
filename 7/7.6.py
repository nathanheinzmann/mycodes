class pessoa():
    def __init__(self, n, i):
        self.nome=n
        self.idade=i
 
class rica(pessoa):
    def __init__(self, n, i, d):
        self.dinheiro=d
        super().__init__(n,i)
    def exibeDados(self):
        print("nome = ", self.nome, ", idade = ", self.idade)
    def fazCompras(self):
        print("faz compras")
class pobre(pessoa):
    def __init__(self, n, i):
        super().__init__(n,i)
    def exibeDados(self):
        print("nome = ", self.nome, ", idade = ", self.idade)
    def trabalha(self):
        print("trabalha")
        
class miseravel(pessoa):
    def __init__(self, n, i):
        super().__init__(n,i)
    def exibeDados(self):
        print("nome = ", self.nome, ", idade = ", self.idade)
    def mendiga(self):
        print("mendiga")

p1 = rica("Ana", 20, 200)
p1.exibeDados()
p1.fazCompras()

p2 = pobre("Noe", 22)
p2.exibeDados()
p2.trabalha()

p3 = miseravel("Pedro", 20)
p3.exibeDados()
p3.mendiga()

