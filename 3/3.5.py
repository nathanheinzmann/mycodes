class professor:
    def __init__(self, A, B, C):
        self.nome = A
        self.disciplina = B
        self.cod = C
        
Ober = professor('Ober','Linguagem de Programacao II',999)

print(Ober.nome, Ober.disciplina)