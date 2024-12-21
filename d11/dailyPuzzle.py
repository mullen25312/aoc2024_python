from dxx.superDailyPuzzle import SuperDailyPuzzle

import collections
from collections import defaultdict

def get_digits(number):
    return [int(num) for num in list(str(number))]

def split_number(number):
    tmp0 = [int(num) for num in list(str(number))]
    tmp1 = int(''.join([str(num) for num in tmp0[:len(tmp0)//2]]))
    tmp2 = int(''.join([str(num) for num in tmp0[len(tmp0)//2:]])) 
    return [tmp1, tmp2]

flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))

# advent of code 2023 day 11
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [int(num) for num in list(self.data.split())]

    def part_one(self, **kwargs):
        stones = self.parsed.copy()

        N = 25
        for idx in range(N):
            for stone_idx, _ in enumerate(stones):
                if stones[stone_idx] == 0: stones[stone_idx] = 1
                elif len(get_digits(stones[stone_idx])) % 2 == 0: stones[stone_idx] = split_number(stones[stone_idx])
                else: stones[stone_idx] *= 2024
            stones = list(flatten(stones))

        self.part_one_result = len(stones)

    def part_two(self, **kwargs):
        stones = self.parsed.copy()

        stone_dict = defaultdict(int)
        for stone in stones:
            stone_dict[stone] += 1

        N = 75
        for idx in range(N):
            stone_dict_diff = defaultdict(int)
            for stone_number in stone_dict:
                if stone_dict[stone_number] == 0: continue
                if stone_number == 0:
                    stone_dict_diff[1] += stone_dict[0]
                elif len(get_digits(stone_number)) % 2 == 0:
                    tmp1, tmp2 = split_number(stone_number)
                    stone_dict_diff[tmp1] += stone_dict[stone_number]
                    stone_dict_diff[tmp2] += stone_dict[stone_number]
                else:
                    stone_dict_diff[stone_number*2024]  += stone_dict[stone_number]

                stone_dict[stone_number] = 0

            for stone_number in stone_dict_diff:
                stone_dict[stone_number] += stone_dict_diff[stone_number]

        self.part_two_result = sum(stone_dict.values())
