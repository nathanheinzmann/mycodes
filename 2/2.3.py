soma=0
negativos=0

for i in range(0,20):
	n = int(input('insira um valor: '))
	if n > 0:
		soma += n
	else:
		negativos += 1
		

		
print('soma dos positivos: ',soma)

print('ha ',negativos, ' numeros negativos')
	