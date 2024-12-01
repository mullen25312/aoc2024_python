from dxx.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

# advent of code 2023 day 1 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        list0 = [int(line.split()[0]) for line in self.data.splitlines()]
        list1 = [int(line.split()[1]) for line in self.data.splitlines()]
        self.parsed = [list0, list1]

    def part_one(self, **kwargs):
        list0 = np.sort(self.parsed[0])
        list1 = np.sort(self.parsed[1])

        self.part_one_result = (abs(list0-list1)).sum()

    def part_two(self, **kwargs):
        list0 = np.array(self.parsed[0])
        list1 = np.array(self.parsed[1])
        
        self.part_two_result = np.array([(list1==element).sum()*element for element in list0]).sum()
