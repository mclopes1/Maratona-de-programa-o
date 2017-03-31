'''
Mariazinha sabe que um Número Primo é aquele que pode ser dividido
somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, 
pois pode ser dividido apenas pelo número 1 e pelo número 7 sem que haja 
resto. Então ela pediu para você fazer um programa que aceite diversos valores 
e diga se cada um destes valores é primo ou não. Acontece que a paciência não é 
uma das virtudes de Mariazinha, portanto ela quer que a execução de todos os casos 
de teste que ela selecionar (instâncias) aconteçam no tempo máximo de um segundo, 
pois ela odeia esperar.
'''
tam = int(input())
count = 0
for i in range(0,tam):
	num = int(input())
	
	if num == 2:
		print ("Prime")
	elif num%2 == 0:
		print ("Not Prime")

	else:
		raiz2 = int(num**(1/2.0)) + 2
		for i in range(2,raiz2):
			if num%i == 0:
				count+= 1
			if count != 0:
				print ("Not Prime")
				break
		if count == 0:
			print ("Prime")
		count = 0

