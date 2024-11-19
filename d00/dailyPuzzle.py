from dxx.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

# advent of code 2023 day 0 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [int(line) for line in self.data.splitlines()]

    def part_one(self, **kwargs):
        input = np.array(self.parsed)
        self.part_one_result = (np.diff(input) > 0).sum()

    def part_two(self, **kwargs):
        input = np.array(self.parsed)
        input_filtered = [(input[idx] + input[idx + 1] + input[idx + 2]) for idx, _ in enumerate(input[0:-2])]
        self.part_two_result = (np.diff(input_filtered) > 0).sum()
