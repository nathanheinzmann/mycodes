passed = []
x = []*15

for i in range(0,15*15):
	x.append(int(input('insira: ')))

for i in range(0,15*15):
	if x.count(x[i])>1:
		print(x[i],'aparece', x.count(x[i]),'vezes')
