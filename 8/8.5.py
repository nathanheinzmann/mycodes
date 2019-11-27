from abc import ABC, abstractmethod 

class Conta(ABC):
    @abstractmethod
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        pass

class ContaInvestimeto(Conta):
    pass