def fatorial(n):
	nf = 1
	if n == 0:
		return 1
	else:
		for i in range(n,0,-1):
			nf = nf * i
	return nf




while True:
	try:
		valores = input()

		valores = valores.split(" ")
		n1,n2 = int(valores[0]),int(valores[1])

		n1 = fatorial (n1)
		n2 = fatorial (n2)

		print(n1+n2)
		
	except(EOFError):
		break
