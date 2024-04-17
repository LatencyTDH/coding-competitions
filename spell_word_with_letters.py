import functools
import collections
from typing import List
import math


class StickerSolver:
    def __init__(self, stickers: List[str], target: str):
        self.stickers = stickers
        self.target = target
        self.target_size = len(target)
        self.stickers = self._prune(self.stickers)
        self.cache = {}

    def _prune(self, stickers):
        target_cnt = collections.Counter(self.target)

        def possible(candidate):
            return bool(target_cnt & collections.Counter(candidate))

        remain = [i for i, sticker in enumerate(stickers) if possible(sticker)]
        final = [stickers[sticker_index] for sticker_index in remain]
        # for sticker_cnt in remain:
        #     add = True
        #     for other in remain:
        #         if sticker_cnt != other and sticker_cnt & other == sticker_cnt:
        #             add = False
        #     if add:
        #         final.append(sticker_cnt)
        return final

    @functools.lru_cache(maxsize=None)
    def _min_stickers(self, tally: int):
        remain_count = tally.bit_count()
        if remain_count == 0:
            return 0

        best_min_stickers = math.inf
        for sticker in self.stickers:
            old_tally = tally
            used_stickers = 1
            for char in sticker:
                for i in range(self.target_size):
                    is_char_match_target_at_index = (
                        self.target[self.target_size - i - 1] == char
                    )
                    is_target_index_unused = (tally & (1 << i)) > 0
                    if is_char_match_target_at_index and is_target_index_unused:
                        tally &= ~(1 << i)
                        break
            if tally.bit_count() < remain_count:
                best_min_stickers = min(
                    best_min_stickers, used_stickers + self._min_stickers(tally)
                )
            tally = old_tally

        return best_min_stickers

    def min_stickers(self):
        target_bitvector = (1 << (self.target_size)) - 1
        minimum = self._min_stickers(target_bitvector)
        return minimum if minimum != math.inf else -1


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        solver = StickerSolver(stickers, target)
        return solver.min_stickers()
