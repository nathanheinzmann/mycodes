from abc import ABC, abstractmethod 

class Animal(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def anda(self):
        pass

class Passaro(Animal):
    def __init__(self):
        pass
    def anda(self):
        pass
    
class Mamifero(Animal):
    def __init__(self):
        pass
    def anda(self):
        pass
    
class BemTeVi(Passaro):
    def anda(self):
        print('Bem Te Vi anda em duas patas')

class Papagaio(Passaro):
    def anda(self):
        print('Papagaio anda em duas patas')
        
class Cachorro(Mamifero):
    def anda(self):
        print('Cachorro anda em quatro patas')
        
class Vaca(Mamifero):
    def anda(self):
        print('Vaca anda em quatro patas')
        
a = BemTeVi()
b = Papagaio()
c = Cachorro()
d = Vaca()

a.anda()
b.anda()
c.anda()
d.anda()
