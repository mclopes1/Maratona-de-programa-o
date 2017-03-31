'''
Neste problema estamos interessados na frequência das letras em uma dada linha de texto.
Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência do texto, 
ignorando o “case sensitive”, ou seja maiúsculas ou minúsculas (sendo mais claro, “letras” 
referem-se precisamente às 26 letras do alfabeto).
'''



tam = int(input())
for i in range(0,tam):
	word = ""
	set_letter = set()
	list_letter = []
	dic = {}
	maior = -1
	text = input()
	text = text.lower()
	for c in text:
		if c != " ":
			if set_letter.__contains__(c) == False:
				amount_c = text.count(c)
				maior = max(amount_c,maior)
				if dic.__contains__(amount_c) == False:
					dic[amount_c] = []
					dic[amount_c].append(c)
				else:
					dic[amount_c].append(c)
				set_letter.add(c)
	dic[maior].sort()
	list_letter = dic[maior]
	for c in list_letter:
		word = word + c

	print (word)