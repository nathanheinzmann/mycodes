#infantil_A = 5 - 7 anos
#infantil_B = 8-10 anos
#juvenil_A = 11-13 anos
#juvenil_B = 14-17 anos
#adulto = maiores de 18 anos

n = int(input('insira a idade:'))

if n>4 and n<8:
    print('Categoria infantil A')
    
elif n>7 and n<11:
    print('Categoria infantil B')

elif n>10 and n<14:
    print('Categoria juvenil A')

elif n>13 and n<18:
    print('Categoria juvenil B')

elif n>17:
    print('Categoria adulto')
    
else: print('Invalido')


