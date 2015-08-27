i = 0

for n in range(2, 100):
	for x in range(2, n):
		if n % x == 0:
			# print(n, 'es igual a', x, '*', n//x)
			break
	else:
		print(n)
		i += 1
print('Se han mostrado', i, 'numeros primos.')
