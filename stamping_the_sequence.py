import re
import unittest

class UnitTester(unittest.TestCase):
	def run_tests(self):
		test_cases = [
			('abca', 'aabcaca'),
			("cab", "cabbb"),
			('abc', 'bbbb', []),
			("mda", "mdadddaaaa", []),
			("a", "a"),
			("zbs", "zbzbsbszbssbzbszbsss"),
		]

		for case in test_cases:
			if len(case) == 3:
				stamp, target, _ = case
				self.assertEqual(movesToStamp(stamp, target), [],
					"Case is impossible but returned a list with numbers!")
			else:
				stamp, target = case
				moves = movesToStamp(stamp, target)
				self.assertTrue(
					verify_sequence(stamp, target, moves),
					f"Failed for stamp: {stamp}, target: {target}, output stamp seq: {moves}")

def movesToStamp(stamp, target):
	start_idx = target.find(stamp)
	if start_idx == -1:
		return []

	solution = []
	end_state = '?' * len(target)
	steps = 0
	replace_length = len(stamp)
	limit = 10 * len(target)
	while target != end_state and steps < limit and start_idx != -1:
		target = target[:start_idx] + '?' * replace_length + target[start_idx + replace_length:]
		# print(target)
		solution.append(start_idx)
		start_idx = determine_next_replacement_index(stamp, target)
		steps += 1

	if len(solution) > limit or target != end_state:
		return []
	else:
		return solution[::-1]

def determine_next_replacement_index(stamp, target):
	stamp_size = len(stamp)
	for start_char in range(stamp_size):
		template = stamp[start_char:]
		new_index = discover(stamp, target, template, -1 * (stamp_size - len(template)))
		# print(template, new_index, -1 * (stamp_size - len(template)))
		if new_index != -1:
			return new_index

	for end_char in range(stamp_size):
		template = stamp[:-end_char]
		new_index = discover(stamp, target, template, 0)
		# print(template, new_index, 0)
		if new_index != -1:
			return new_index

	return -1

def discover(stamp, target, substring, adjustment_dist):
	matches = re.finditer(substring, target)
	for match in matches:
		potential_idx = match.start()
		if potential_idx != -1:
			new_start = potential_idx + adjustment_dist
			new_end = new_start + len(stamp)
			if new_start >= 0 and new_end <= len(target) and can_replace(target[new_start:new_end], stamp):
				return new_start
	return -1

def can_replace(templified_str, stamp):
	for idx, ch in enumerate(stamp):
		if templified_str[idx] != '?' and ch != templified_str[idx]:
			return False
	return True

def verify_sequence(stamp, target, sequence):
	blank_slate = ['?'] * len(target)
	stamp_size = len(stamp)
	for index in sequence:
		blank_slate[index:index+stamp_size] = stamp
	return ''.join(blank_slate) == target


if __name__ == '__main__':
	UnitTester().run_tests()
