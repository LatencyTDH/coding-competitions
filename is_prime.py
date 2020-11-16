import sys

def is_prime(num):
	if num < 2:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	i = 3
	while i * i <= num:
		if num % i == 0:
			return False
		i += 2
	return True

def test_1():
	count = 0
	for i in range(1000):
		count += 1 if is_prime(i) else 0
	assert count == 168

if __name__ == '__main__':
	print(is_prime(int(sys.argv[1])))
