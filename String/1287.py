'''
Computadores estão presentes em uma porcentagem significante de casas pelo mundo e, como programadores,
somos responsáveis por criar interfaces que todos possam usar. Interfaces de usuário precisam ser 
flexíveis de forma que se um usuário comete um erro não fatal, a interface ainda pode deduzir o 
que o usuário queria dizer.

Sua tarefa é escrever um programa que processe um texto de entrada representando um inteiro, 
porém, como esta é uma interface de usuário, não seremos muito rígidos com o usuário:

1. Se o usuário digita a letra "O" ou "o", assumimos que ele queria digitar o número "0".

2. Se o usuário digita a letra "l", assumimos que ele queria digitar o número "1".

3. Vírgulas e espaços são permitidos, porém não são processados (são ignorados).

Se, mesmo com as regras acima, o usuário não entrou um número não-negativo, imprima a string "error". Overflow (um valor maior que 2147483647) é considerado inválido e "error" deve ser impresso.
'''
while True:
	try:
		new_number = ""
		number = input()
		for letter in number:
			if letter == "l":
				new_number = new_number + "1"
			elif letter in "oO":
				new_number = new_number + "0"
			elif letter != " " and letter != ",":
				new_number = new_number + letter
		if new_number.isnumeric() == False:
			print ("error")
		elif int(new_number) > int("2147483647"):
			print ("error")
		else:
			print (str(int(new_number)))
	except(EOFError):
		break