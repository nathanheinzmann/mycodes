v1 = []
v2 = []

for i in range (0,20):
	if i <10:
		v1.append(int(input('Insira no Vetor 1:')))
	else:
		v2.append(int(input('Insira no Vetor 2:')))
v3 = v1+v2

print(v3)