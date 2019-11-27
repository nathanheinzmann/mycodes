class Empregado:
    def __init__(self, A, B, C, D):
        self.nome = A
        self.departamento = B
        self.horasTrabalhadasNoMês = C
        self.salárioPorHora = D
    def mostraDados(self):
        print('Nome = ', Jorge.nome, '\nDepartamento = ', Jorge.departamento, '\nHoras trabalhadas no mes = ',Jorge.horasTrabalhadasNoMês, '\nSalario por hora = ', Jorge.salárioPorHora )
    def calculaSalarioMensal(self):
        print('Salario mensal = ',Jorge.horasTrabalhadasNoMês * Jorge.salárioPorHora)


Jorge = Empregado('Jorge', 'RH', 120, 20)

print(Jorge.mostraDados(), Jorge.calculaSalarioMensal())
