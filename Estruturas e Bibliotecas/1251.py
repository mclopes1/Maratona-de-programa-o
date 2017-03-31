
lista = []
saida = []
sensor = 0
dic = {}
i = 0
while True:
	try:
		text = input()
		for c in text:
			if lista.__contains__(c) == False:
				lista.append(c)
				saida.append(str(ord(c)) + " " + str(text.count(c)))
		saida.sort()
		dic[i] = saida
		i = i + 1 
		saida = []
		lista = []
	except (EOFError):
		for j in range(0,len(dic)):
			if j != len(saida[l]) - 1:
				saida = dic[j]
				for l in range(len(saida) - 1,-1,0):
					print (saida[l])
				print ("\n")
			elif j == (len(dic) - 1):
				saida = dic[j]
				for l in range(len(saida) - 1,-1,0):
					print (saida[l])

		break

