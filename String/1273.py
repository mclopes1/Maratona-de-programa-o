text = ""
qtdEntry = int(input())
while True:
	ps = []
	atual = 0
	
	for i in range(0,qtdEntry):
		ps.append(input())

	if qtdEntry != 0:
		maior = (len(max(ps)))

	for i in range(0,qtdEntry):
		text = (maior - len(ps[i]))*' ' + ps[i]
		print (text)

	qtdEntry = int(input())
	if qtdEntry == 0:
		break
	else:
		print ()