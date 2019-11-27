import os

n = int(input("Insira um valor(-1 para SAIR): "))

while n != -1:
	cont = 0
	for i in range (2, n):
		if n%i == 0:
			cont+=1
			
	if cont == 0:
		print('\neh primo\n\n')
	else:
		print('\nnao eh primo\n\n')

	n = int(input("Insira um valor: \n (-1 para SAIR): "))
