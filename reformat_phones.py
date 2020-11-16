import re

hyph_reg = re.compile(r'([0-9]{3})-([0-9]{3})-([0-9]{4})')
single_reg = re.compile(r'([0-9]{3})([0-9]{3})([0-9]{4})')
reg_replaces = [(hyph_reg, r'\2-\1-\3'), (single_reg, r'\2\1\3')]

def reformat(phone_nums):
	for idx, pn in enumerate(phone_nums):
		for reg, repl in reg_replaces:
			if pn and reg.match(pn):
				phone_nums[idx] = re.sub(reg, repl, pn)

if __name__ == "__main__":
	phone_nums = ['3667708967', '366-770-8967', '', '366-(770)8967', None]
	reformat(phone_nums)
	print(phone_nums)
	assert phone_nums == ['7703668967', '770-366-8967', '', '366-(770)8967', None]
	