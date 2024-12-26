from dxx.superDailyPuzzle import SuperDailyPuzzle

import itertools
import numpy as np

# advent of code 2023 day 25
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        keys = []; locks = []
        self.data = self.data + '\n\n'

        tmp = []
        for line in self.data.splitlines():
            if line == '':
                if tmp[0] == '#####': locks.append([row.count('#') - 1 for row in [list(i) for i in zip(*tmp)]])
                else: keys.append([row.count('#') - 1 for row in [list(i) for i in zip(*tmp)]])
                tmp = []; continue
            tmp.append(line)

        self.parsed = keys, locks
           
    def part_one(self, **kwargs): 
        keys, locks = self.parsed
        self.part_one_result = [((np.array(key) + np.array(lock)) < 6).all() for key,lock in itertools.product(keys, locks)].count(True)

    def part_two(self, **kwargs):   
        self.part_two_result = 0
