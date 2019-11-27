class ingresso():
    def __init__(self, v):
        self.valor=v
    def imprimeValor(self):
        print("valor = ", self.valor)

class vip(ingresso):
    def __init__(self, v, a):
        self.adicional=a
        super().__init__(v)
    def getValorAdicional(self):
        return self.valor+self.adicional
 
class normal(ingresso):
    def __init__(self, v):
        super().__init__(v)
    def valorNormal(self):
        print("Normal: valor = ", self.valor)
 
class camaroteInferior(vip):
    def __init__(self, v, l, a):
        self.localizacao=l
        super().__init__(v, a)
    def imprimeInferior(self):
        print("Inferior: valor = ", self.valor, ", localizacao = ", self.localizacao)
 
class camaroteSuperior(vip):
    def __init__(self, v, a):
        self.adicional=a
        super().__init__(v, a)
    def imprimeSuperior(self):
        print("Superior: valor + adicional = ", self.valor+self.adicional)
 

i1 = vip(50, 30)
print("Vip + adicional = ", i1.getValorAdicional())

i2 = normal(40)
i2.valorNormal()

i3 = camaroteInferior(50, "Inferior 1", 5)
i3.imprimeInferior()

i4 = camaroteSuperior(50, 10)
i4.imprimeSuperior()