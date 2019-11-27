s=0
p=1

for i in range(0,20):
	n = int(input('insira um valor: '))
	if n%2==0:
		s+=n
	else:
		p*=n
		

		
print('soma dos pares: ', s)

print('produto dos impares: ', p)
	