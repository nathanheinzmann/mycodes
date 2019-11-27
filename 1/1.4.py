n = int(input('Insira o tempo em seg:'))
h=m=s=0

while n >= 3600:
    h+=1
    n-=3600

while n >= 60:
    m+=1
    n-=60
s=n

print(h,'horas',m,'minutos e ',s,'segundos')