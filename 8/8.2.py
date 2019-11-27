from abc import ABC, abstractmethod 

class Conta(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def atualiza(self):
        pass