class Livro:
    def __init__(self, A, B, C, D):
        self.nome = A
        self.autor = B
        self.paginas = C
        self.ano = D

livro1 = Livro('O Pequeno Principe', 'Antoine de Saint-Exupery', 230, 1943)
print('Musica = ', livro1.nome, '\nAutor = ', livro1.autor, '\nPaginas = ', livro1.paginas, '\nAno = ', livro1.ano)
