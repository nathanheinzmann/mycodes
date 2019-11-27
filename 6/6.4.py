class pessoa():
    def __init__(self, n, e):
        self.nome = n
        self.end = e
    
    def getNome(self):
        return self.nome
    
    def getEnd(self):
        return self.end
    
    def setNome(self, n):
        self.nome = n
        
    def setEnd(self, e):
        self.end = e
        
class cliente(pessoa):
    def __init__(self, n, e, c, ved):
        pessoa.__init__(self, n, e)
        self.credimaximo = c
        self.valorEmDivida = ved
    
    def getCredimaximo(self):
        return self.credimaximo
    
    def getValorEmDivida(self):
        return self.valorEmDivida
    
    def setCredimaximo(self, c):
        self.credimaximo = c
        
    def setValorEmDivida(self, ved):
        self.valorEmDivida = ved
    
    def obterSaldo(self):
        return(self.credimaximo - self.valorEmDivida)
        
        
x = cliente("Nathan", "SLG", 50, 15)
print(x.obterSaldo())
x.setCredimaximo(200)
print(x.obterSaldo())
