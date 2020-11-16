import unittest

class UnitTester(unittest.TestCase):
	def run_tests(self):
		test_cases = [
			("++++", True),
			("+++", True),
			("+", False),
			("", False),
			("+--++", True),
			("+++++", False),
			("++++--++++", False),
			("++++++++++", True),
			("+++++-", False),
		]

		for case in test_cases:
			board, winnable = case
			self.assertEqual(canWin(board), winnable, f"string: {board}, expected isWinnable: {winnable}")

def canWin(s: str) -> bool:
	if len(s) <= 1: return False
	return True

if __name__ == '__main__':
	UnitTester().run_tests()