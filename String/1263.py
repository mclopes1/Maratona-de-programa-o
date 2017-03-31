while True:
	try:
		count = 0
		j = -1
		text = input()
		text = text.lower()
		text = text.split(" ")
		final = len(text) - 1
		for i in range(0,len(text)):

			if j != i and i != final:
				if text[i][0] == text[i+1][0]:
					count = count + 1
					j = i + 1
		print (count)
	except(EOFError):
		break

