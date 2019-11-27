from abc import ABC, abstractmethod 

class Conta(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def atualiza(self):
        pass
if __name__ == '__main__':
    c = Conta()

#Não é possível instanciar um objeto na classe abstrata, seria necessário
#criar uma classe concreta que herda de 'Conta' para instanciar esse objeto.