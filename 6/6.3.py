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
        
class empregado(pessoa):
    def __init__(self, n, e, sb, mt):
        pessoa.__init__(self, n, e)
        self.salarioBase = sb
        self.mesesTrabalhados = mt
    
    def getSalarioBase(self):
        return self.salarioBase
    
    def getMesesTrabalhados(self):
        return self.mesesTrabalhados
    
    def setSalarioBase(self, sb):
        self.salarioBase = sb
        
    def setMesesTrabalhados(self, mt):
        self.mesesTrabalhados = mt
    
    def calcularSalario(self):
        return(self.mesesTrabalhados * self.salarioBase)
        
        
x = empregado("Nathan", "SLG", 2000, 8)
print(x.calcularSalario())
x.setMesesTrabalhados(200)
print(x.calcularSalario())
