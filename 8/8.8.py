from abc import ABC, abstractmethod 

class Conta(ABC):
    @abstractmethod
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        pass

class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        super().__init__(numero, titular, saldo, limite)
    def deposita(self, saldo):
        self._saldo += self._saldo
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

ci = ContaInvestimento('123-6', 'Maria', 1000)
ci.deposita(1000.0)
ci.atualiza(0.01)
print(ci._saldo)