from math import log2
import sys

def solve_10(num_bits):
	bitarray = [0] * num_bits
	for i in range(1, num_bits + 1):
		print(i, flush=True)
		resp = int(input())
		bitarray[i - 1] = resp

	bitstring = "".join(map(str, bitarray))
	print(bitstring, flush=True)
	resp = input()
	if resp == 'N':
		exit(1)

def solve_20(num_bits):
	sys.stderr.write("OUTPUTTING " + str(num_bits) + '\n')
	bitarray = [0] * num_bits
	states = []
	for i in range(1, num_bits + 1):
		if i % 10 == 1 and i > 1:
			pass
		print(i, flush=True)
		resp = int(input())
		bitarray[i - 1] = resp

		if i == 10:
			states.append(bitarray.copy())
		elif i == 20:
			states.append(bitarray.copy())

	bitstring = "".join(map(str, bitarray))
	sys.stderr.write("OUTPUTTING " + str(bitstring) + '\n')
	print(bitstring, flush=True)
	resp = input()
	if resp == 'N':
		exit(1)
		sys.stderr.write("Wrong answer!\n")

def solve(num_bits):
	sys.stderr.write("OUTPUTTING " + str(num_bits) + '\n')
	bitarray = [0] * num_bits
	for i in range(1, num_bits + 1):
		print(i, flush=True)
		resp = int(input())
		bitarray[i - 1] = resp

	bitstring = "".join(map(str, bitarray))
	sys.stderr.write("OUTPUTTING " + str(bitstring) + '\n')
	print(bitstring, flush=True)
	resp = input()
	if resp == 'N':
		sys.stderr.write("Wrong answer!\n")
		exit(1)


def entropy(vector):
    tot = sum(vector)
    normed = [x/tot for x in vector]
    return -sum(prob * log2(prob) for prob in normed if prob != 0)

def main():
	tcs, num_bits = map(int, input().split())
	for case in range(1, tcs + 1):
		if num_bits == 10:
			solve_10(num_bits)
		elif num_bits == 20:
			solve_20(num_bits)
		else:
			solve(num_bits)

if __name__ == '__main__':
	main()