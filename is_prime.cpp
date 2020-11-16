#include <iostream>

typedef unsigned long long ull;

bool is_prime(const ull num) {
	if (num < 2) {
		return false;
	}
	if (num == 2) {
		return true;
	}
	if ((num % 2) == 0) {
		return false;
	}
	ull i = 3;
	while (i * i <= num) {
		if (num % i == 0) {
			return false;
		}
		i += 2;
	}
	return true;
}

int main(int argc, char** argv) {
	std::cout << is_prime(std::stoull(argv[1])) << std::endl;
	return 0;
}
