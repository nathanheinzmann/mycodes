cq = 1.200
bs = 1.300
bco = 1.500
h = 1.200
c = 1.300
r = 1.00

n = int(input('Insira o codigo do pedido: '))
x = int(input('Insira a quantidade: '))


if n == 100:
    print('Valor = ', round((cq*x),3))
elif n == 101:
    print('Valor = ', round((bs*x),2))
elif n == 102:
    print('Valor = ', round((bco*x),2))
elif n == 103:
    print('Valor = ', round((h*x),2))
elif n == 104:
    print('Valor = ', round((c*x),2))
elif n == 105:
    print('Valor = ', round((r*x),2))