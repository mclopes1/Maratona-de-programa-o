def simplifica(nf,df):
	i = 2
	nfs = nf
	dfs = df
	while i <= abs(nfs) and i <= abs(dfs):
		if nfs%i == 0 and dfs%i == 0:
			nfs = nfs/i
			dfs = dfs/i
		else: i = i + 1
	print ("%d/%d = %d/%d"%(nf,df,nfs,dfs))


tam = int(input())

for i in range(0,tam):
	expression = input()

	expression = expression.split(" ")

	n1,d1,op,n2,d2 = int(expression[0]),int(expression[2]),expression[3],int(expression[4]),int(expression[6])

	if op == "+":
		nf = (n1*d2 + n2*d1)
		df = (d1*d2)
		simplifica(nf,df)

	elif op == "-":
		nf = (n1*d2 - n2*d1)
		df = (d1*d2)
		simplifica(nf,df)

	elif op == "*":
		df = d1*d2
		nf = n1*n2
		simplifica(nf,df)
	
	elif op == "/":
		nf = n1 * d2
		df = d1 * n2
		simplifica(nf,df)