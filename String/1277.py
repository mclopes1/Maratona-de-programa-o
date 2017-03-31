'''Os estudantes da tua universidade recentemente
 adquiriram o desagradável hábito de cabular as aulas.
 Para enfrentar este problema o seu Conselho de Professores 
 decidiu somente permitir que estudantes com ao menos 75% de 
 presença prestem os exames. A partir de uma lista de nomes 
 de estudantes e seus respectivos registros de frequência, 
 imprima o nome dos estudantes que não obtiveram o mínimo de 
 presença às aulas e que consequentemente não poderão prestar 
 os exames.
ENTRADA										SAIDA
4											Justin
1											Justin
Justin									    
PPPAAAMPP									Arjun Nikhil Taneja
2											
Justin Chris
PAAPP PPPPA
1
Sunny
PPPAM
4
Mansi Arjun Nikhil Taneja
PPPPMPPAPP AAMAAPP PPPPAAP PPPAAAMPP''' 


tam = int(input())
for i in range(0,tam):
	all_reproved_student = ""
	qtd = int(input())
	student = input()
	register = input()
	student = student.split(" ")
	register = register.split(" ")
	len_Student = len(student)
	for i in range(0,len_Student):
		P = float(register[i].count("P"))
		M = float(register[i].count("M"))
		A = float(register[i].count("A"))
		if (P*100)/(P+A) < 75:
			all_reproved_student = all_reproved_student + student[i] + " "
	all_reproved_student = all_reproved_student.strip(" ")
	print (all_reproved_student)