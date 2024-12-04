from dxx.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
import re

pattern0 = r"\d{1,3}"
pattern1 = r"mul\(\d{1,3},\d{1,3}\)"
pattern2 = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

def check_safety(report):
    return ((report == np.sort(report)).all() or (report == np.flip(np.sort(report))).all()) and (0 < abs(np.diff(report))).all() and (abs(np.diff(report)) <= 3).all()

# advent of code 2023 day 3 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = self.data

    def part_one(self, **kwargs):
        matches = re.findall(pattern1, self.parsed)
        self.part_one_result = sum([np.prod([int(number) for number in re.findall(pattern0, match)]) for match in matches])

    def part_two(self, **kwargs):
        matches = re.findall(pattern2, self.parsed)

        res2 = 0
        enabled = True
        for match in matches:
            if match == "don't()": enabled = False
            elif match == "do()": enabled = True
            else: res2 += np.prod([int(number) for number in re.findall(pattern0, match)])*(enabled == True)

        self.part_two_result = res2