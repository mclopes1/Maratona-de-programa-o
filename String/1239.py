

while True:
	try:
		phrase = input()
		newPhrase = ""
		sensorNeg = 0
		sensorIta = 0


		for c in phrase:

			if c == "_" and sensorIta == 0:
				newPhrase = newPhrase + "<i>" 
				sensorIta = 1
			elif c == "_" and sensorIta == 1:
				newPhrase = newPhrase + "</i>" 
				sensorIta = 0
			elif c == "*" and sensorNeg == 0:
				newPhrase = newPhrase + "<b>"
				sensorNeg = 1
			elif c == "*" and sensorNeg == 1:
				newPhrase = newPhrase + "</b>"
				sensorNeg = 0
			else:
				newPhrase = newPhrase + c
		print (newPhrase)
	except(EOFError):
		break


