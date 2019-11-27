from abc import ABC, abstractmethod 

class Item(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def empresta(self):
        pass
    def retorna(self):
        pass

class Livro(Item):
    def __init__(self):
        pass
    def bloqueia(self):
        pass
    def desbloqueia(self):
        pass
    
class ItemRestrito(Item):
    def __init__(self):
        pass
    def alteraNivel(self):
        pass
    
class Periodico(Livro):
    def empresta(self):
        print('empresta')
    def retorna(self):
        print('retorna')
    def bloqueia(self):
        print('bloqueia')
    def desbloqueia(self):
        print('desbloqueia')

class Fita(ItemRestrito):
    def empresta(self):
        print('empresta')
    def retorna(self):
        print('retorna')
    def alteraNivel(self):
        print('altera nivel')
    
class SalaEstudo(ItemRestrito):
    def empresta(self):
        print('empresta')
    def retorna(self):
        print('retorna')
    def alteraNivel(self):
        print('altera nivel')

a = Periodico()
b = Fita()
c = SalaEstudo()
a.empresta()
b.retorna()
c.alteraNivel()