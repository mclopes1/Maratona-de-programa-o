def to_bin(num):
	resto = ""
	if num == 1:
		return "1"
	elif num == 0:
		return "0"
	else:
		while num != 1:
			quociente = int(num/2)
			resto = resto + str((num%2))
			num = quociente
	resto = resto + str(num)
	return resto[::-1]

while True:
	try:
		num = input()
		num = num.split(" ")
		
		num,num2 = num[0],num[1]
		
		num = to_bin(int(num))
		num2 = to_bin(int(num2))

		new_number = ""
		length_num = len(num)
		length_num2 = len(num2)
		
		if length_num > length_num2:
			tam = length_num - 1
			num2 = '0'*(length_num - length_num2) + num2
		elif length_num2 > length_num:
			tam = length_num2 - 1
			num = '0'*(length_num2 - length_num) + num
		else:
			tam = length_num - 1

		for i in range(tam,-1,-1):
			if num[i] == '0' and num2[i] == '0':
				new_number = '0' + new_number
			elif num[i] == '0' and num2[i] == '1':
				new_number = '1' + new_number
			elif num[i] == '1' and num2[i] == '0':
				new_number = '1' + new_number
			elif num[i] == '1' and num2[i] == '1':
				new_number = '0' + new_number

		print (int(new_number,2))

	except(EOFError):
		break