def divisible_3(numstr):
	total = 0
	addend = 1
	for bit in numstr:
		total += int(bit) * addend
		addend = -1 * addend
		if total == 3 or total == -3:
			total = 0

	return total == 0


if __name__ == '__main__':
	total = 0
	for i in range(6):
		bitstring = str(bin(i))[2:]
		divisible = divisible_3(bitstring)
		# print(bitstring, divisible)
		total += divisible
	print(f"Found {total} divisible by 3 bitstrings between range")
	print(divisible_3('11101010101010101111111111100101010101011001010101111111010100101010101010101010101010101010'))