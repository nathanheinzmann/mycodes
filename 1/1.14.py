x = input('"f" para entrar com Fahrenheit | "c" para entrar com Celsius |\n Insira a letra:')
t = int(input('Insira o valor da temperatura: '))


if x == 'c':
    print(((9/5)*t+32), 'graus F')
    
else: print(((5/9)*(t-32)), 'graus C')