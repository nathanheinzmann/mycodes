
from abc import ABC, abstractmethod 

class Conta(ABC):
    @abstractmethod
    def __init__(self, n, t, s=0, l=1000.0):
        pass
class ContaCorrente(Conta):
    def __init__(self, n, t, s=0, l=1000.0):
        self._numero = n
        self._titular = t
        self._saldo = s
        self._limite = l
        super().__init__(n, t, s, l)

    def atualiza(self, s):
        self._saldo = s
        
        
class ContaPoupanca(Conta):
    def __init__(self, n, t, s=0, l=1000.0):
        self._numero = n
        self._titular = t
        self._saldo = s
        self._limite = l
        super().__init__(n, t, s, l)

    def atualiza(self, saldo):
        self._saldo = saldo
        
    
if __name__ == '__main__':
            cc = ContaCorrente('123-4', 'João', 1000.0)
            cp = ContaPoupanca('123-5', 'José', 1000.0)
            cc.atualiza(0.01)
            cp.atualiza(0.01)
            print(cc._saldo)
            print(cp._saldo)