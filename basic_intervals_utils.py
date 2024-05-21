def get_overlap(range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int] | None:
    low1, high1 = range1
    low2, high2 = range2
    if not (low2 <= high1 and low1 <= high2): return None
    return (max(low1, low2), min(high1, high2))

assert get_overlap((1, 11), (2, 13)) == (2, 11)
assert get_overlap((2, 13), (1, 11)) == (2, 11)
assert get_overlap((1,1), (2,2)) == None
assert get_overlap((2, 2), (2, 2)) == (2, 2)
assert get_overlap((1,1), (-10, 10)) == (1, 1)
assert get_overlap((15, 20), (17, 19)) == (17, 19)