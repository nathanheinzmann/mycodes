import os
win=0
pos = int(input('Insira a posicao do Marciano: '))

os.system('clear')

for i in range(0,5):
	tiro = int(input('escolha o numero da arvore p/ atirar: '))

	if tiro > pos:
		print('estou mais a esquerda\n')
	elif tiro < pos:
		print('estou mais a direita\n')
	else:
		print('voce acertou o marciano! :D')
		win+=1
		break
if win==0:
	print('voce foi abduzido para marte "LOSER"')
