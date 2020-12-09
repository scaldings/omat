def uloha1():
	pass


def uloha2():
	for x in range(1, 1000000):
		for y in range(1, 10):
			number = (x / y) + 1
			x_num = str(number)[0]
			y_num = str(number).split('.')[1][0:3]
			if (y_num == str(y) * 3) and (x_num == str(x)):
				print('*' * 20)
				print(f'{x_num}.{y_num} == {number}')
				print(f'x = {x}')
				print(f'y = {y}')
				print('*' * 20)


def uloha4():
	for x in range(10000, 99999):
		string = str(x)
		for y in range(0, len(string) + 1):
			for z in range(0, len(string) + 1):
				result1 = int(string[:y] + '1' + string[y:])
				result2 = int(string[:z] + '1' + string[z:])
				if (result2 == (result1  * 3)):
					print(x)
					print(f'{result2} == {result1} * 3')
				elif (result1 == (result2  * 3)):
					print(x)
					print(f'{result1} == {result2} * 3')
