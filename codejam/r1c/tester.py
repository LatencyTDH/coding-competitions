from random import randint

def main():
	upper = 10 ** 16 - 1
	template = 'SEANTDIPYZ'
	f = open('custom_test.txt', 'w')
	f.write('1\n')
	f.write('16\n')

	for _ in range(10 ** 4):
		num = randint(1, upper)
		ni = randint(1, num)
		ni = str(ni)
		res = ''
		for digit in ni:
			res += template[int(digit)]
		f.write(f"-1 {res}\n")
	f.close()

if __name__ == '__main__':
	main()