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

