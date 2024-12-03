from dxx.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

def check_safety(report):
    return ((report == np.sort(report)).all() or (report == np.flip(np.sort(report))).all()) and (0 < abs(np.diff(report))).all() and (abs(np.diff(report)) <= 3).all()

# advent of code 2023 day 2 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [np.array([int(num) for num in line.split()]) for line in self.data.splitlines()]

    def part_one(self, **kwargs):
        self.part_one_result = [check_safety(report) for report in self.parsed].count(True)

    def part_two(self, **kwargs):
        self.part_two_result = [(check_safety(report) or np.array([check_safety(np.delete(report, idx)) for idx in range(0, len(report))]).any()) for report in self.parsed].count(True)