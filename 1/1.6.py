import math

x1 = int(input('insira x1: '))
y1 = int(input('insira y1: '))
x2 = int(input('insira x2: '))
y2 = int(input('insira y2: '))

y=(pow((x2-x1),2)+pow((y2-y1),2))

print('distancia entre os 2 pontos: ',math.sqrt(y))