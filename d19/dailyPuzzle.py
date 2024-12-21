from dxx.superDailyPuzzle import SuperDailyPuzzle

import functools

@functools.lru_cache
def match_pattern(design, patterns):
    if design == '': return 1
    else: return sum([match_pattern(design[len(pattern):], patterns) if design.startswith(pattern) else 0 for pattern in patterns])

# advent of code 2023 day 19
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = self.data.splitlines()
        patterns = tuple([pattern.strip() for pattern in self.data.splitlines()[0].split(',')])
        designs = tuple([design.strip() for design in self.data.splitlines()[2:]])
        self.parsed = [patterns, designs]
           
    def part_one(self, **kwargs): 
        patterns, designs = self.parsed
        self.part_one_result = len(designs) - [match_pattern(design, patterns) for design in designs].count(0)

    def part_two(self, **kwargs): 
        patterns, designs = self.parsed
        self.part_two_result = sum([match_pattern(design, patterns) for design in designs])
