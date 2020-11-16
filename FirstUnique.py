class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freq_of_num = {}
        self.uniq_queue = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if not self.uniq_queue:
            return -1

        return next(iter(self.uniq_queue))

    def add(self, value: int) -> None:
        if value not in self.freq_of_num:
            self.freq_of_num[value] = 1
            self.uniq_queue[value] = 1
        else:
            if value in self.uniq_queue:
                del self.uniq_queue[value]
            self.freq_of_num[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)