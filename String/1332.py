tam = int(input())
for i in range(0,tam):
	number = input()
	if len(number) == 5:
		print ("3")
	elif number.__contains__("t") == True and number.endswith("o") == True:
		print ("2")
	elif number.__contains__("e") and number.startswith("o") == True:
		print ("1")
