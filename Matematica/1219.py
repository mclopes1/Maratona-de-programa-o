#Falta coisa :(


def resultadoAreaTriaReta(ca1,ca2,hip):
	raioMenor = (ca1 + ca2 - hip)/2.0
	ciareaMenor = (raioMenor**2)*pi

	perimetroTriangulo = (ca1 + ca2 + hip)/2
	areaTriangulo = (perimetroTriangulo*(perimetroTriangulo - ca1)*(perimetroTriangulo - ca2)*(perimetroTriangulo - hip))**(1/2.0)
	areaTriangulo = areaTriangulo - ciareaMenor

	raioMaior = hip/2.0
	areaCircMaior = pi*(raioMaior**2)
	areaCircMaior = areaCircMaior - areaTriangulo - ciareaMenor

	print ("%.4f %.4f %.4f" %(areaCircMaior,areaTriangulo,ciareaMenor))

def resultadoTriaNotRetan(l1,l2,l3):
	perimetroTriangulo = (l1 + l2 + l3)/2.0
	areaTriangulo = (perimetroTriangulo*(perimetroTriangulo - l1)*(perimetroTriangulo - l2)*(perimetroTriangulo - l3))**(1/2.0)
	
	raioMenor = areaTriangulo/perimetroTriangulo
	ciareaMenor = (raioMenor**2)*pi

	areaTriangulo = areaTriangulo - ciareaMenor

	

	raioMaior = l2/2.0
	areaCircMaior = pi*(raioMaior**2)
	areaCircMaior = areaCircMaior - areaTriangulo - ciareaMenor

	print ("%.4f %.4f %.4f" %(areaCircMaior,areaTriangulo,ciareaMenor))



pi = 3.1415926535897
while True:
	try:
		valores = input()

		valores = valores.split(" ")

		l1,l2,l3 = int(valores[0]),int(valores[1]),int(valores[2])

		if l1**2 + l2**2 == l3**2:
			resultadoAreaTriaReta(l1,l2,l3)
		else: 
			resultadoTriaNotRetan(l1,l2,l3)
	except(EOFError):
		break