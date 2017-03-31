'''Implemente um programa denominado combinador, 
que recebe duas strings e deve combiná-las, alternando 
as letras de cada string, começando com a primeira letra 
da primeira string, seguido pela primeira letra da segunda
 string, em seguida pela segunda letra da primeira string, 
 e assim sucessivamente. As letras restantes da cadeia mais 
 longa devem ser adicionadas ao fim da string resultante e retornada.'''
tam = int(input())

for i in range(0,tam):
	new_text = ""
	text = input()
	text = text.split(" ")
	maior = max(len(text[0]),len(text[1]))
	menor = min(len(text[0]),len(text[1]))

	for i in range(0,maior):
		if i < menor:
			new_text = new_text + text[0][i] + text[1][i]
		else:
			if maior == len(text[0]):
				new_text = new_text + text[0][i]
			else:
				new_text = new_text + text[1][i] 
	print (new_text)