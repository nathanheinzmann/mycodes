class imovel():
    def __init__(self, e, p):
        self.endereco=e
        self.preco=p
    
    def imprimeValor(self):
        print("valor = ", self.valor)

class novo(imovel):
    def __init__(self, e, p, a):
        self.adicional=a
        super().__init__(e, p)
    def getValorNovo(self):
        return self.preco+self.adicional
 
class velho(imovel):
    def __init__(self, e, p, d):
        self.desconto=d
        super().__init__(e, p)
    def getValorVelho(self):
        return self.preco-self.desconto
 
 
i1 = novo("Rua Nova", 500, 200)
print("valor do novo c/ adicional = ", i1.getValorNovo())

i2 = velho("Rua Velha", 500, 100)
print("valor do velho c/ desconto = ", i2.getValorVelho())