class Pair {
	public:
		Pair() {}
		Pair(char firstValue, char secondValue) :
			firstValue(firstValue), secondValue(secondValue) {}
		char getFirst() {
			return first;
		}
	private:
		char first;
		char second;
}