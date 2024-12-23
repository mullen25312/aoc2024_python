from dxx.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict

import numpy as np
import itertools 

def next(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret

def array_match(a, b):
    for i in range(0, len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return i
    return None

# advent of code 2023 day 22
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [int(num) for num in self.data.splitlines()]
           
    def part_one(self, **kwargs): 
        tmp = self.parsed.copy()

        # generate secrets
        N = 2000 + 1
        secrets = [[0 for _ in range(len(tmp))] for _ in range(N)]
        secrets[0] = tmp
        for n in range(1, N):
            for idx, _ in enumerate(secrets[-1]):
                secrets[n][idx] = next(secrets[n-1][idx])
        self.temp = secrets # save secrets for part 2

        self.part_one_result = sum(secrets[-1])

    def part_two(self, **kwargs): 
        secrets = self.temp

        # get prices and price diffs from secrets
        prices = [[secret % 10 for secret in row] for row in secrets]
        diffs = np.diff(np.transpose(prices))

        # index diffs
        diff_index = [defaultdict(list) for _ in range(len(diffs))]
        for idx, diff in enumerate(diffs):
            for i in range(0, len(diff)-4):
                diff_index[idx][(diff[i], diff[i+1],diff[i+2],diff[i+3])].append(i)

        # find best sequence
        res2 = 0
        for seq in set([tuple(np.diff(tmp)) for tmp in itertools.product(range(0,10), repeat=5)]):
            tmp = 0
            for idx, diff in enumerate(diffs):
                best = diff_index[idx][seq]
                if best != []: tmp += prices[best[0]+4][idx]
            if tmp > res2: res2 = tmp

        self.part_two_result = res2
