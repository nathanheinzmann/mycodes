# Implemente a classe Funcionario e a classe Gerente.
# crie a classe Assistente, que também é um funcionário, e que possui um número de matrícula (faça o método GET).
# Sobrescreva o método exibeDados(). sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes
# Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e Administrativo.

class funcionario():
    def __init__(self, n, i, s):
        self.nome=n
        self.idade=i
        self.salario=s
    def exibeDados(self):
        print("nome = ", self.nome, ", idade = ", self.idade, ", salario = ", self.salario)
class gerente():
    pass
 
class assistente(funcionario):
    def __init__(self, n, i, s, m):
        self.matricula=m
        super().__init__(n,i,s)
    
    def getMatricula(self):
        return self.matricula
    def exibeDados(self):
        print("nome = ", self.nome, ", idade = ", self.idade, ", salario = ", self.salario, ", matricula = ", self.matricula)
class tec(assistente):
    def __init__(self, b, n, i, s, m):
        self.bonus=b
        super().__init__(n,i,s,m)
class adm(assistente):
    def __init__(self, m, n, i, s, t, ad):
        self.turno=t
        self.adicional=ad
        super().__init__(n,i,s,m)

p1 = funcionario("Ana", 21, 1000)
p1.exibeDados()
p2 = assistente("Noe", 22, 2000, 1234)
p2.exibeDados()
