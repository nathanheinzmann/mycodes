n = int(input('Insira o tempo da ligacao: '))
if n > 3:
    print('total: ', (((n-3)*0.26)+1.15))
else: print('1.15')