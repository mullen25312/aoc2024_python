from dxx.superDailyPuzzle import SuperDailyPuzzle

import re
pattern0 = r'\d+'

def find_tokens(prize, offset):
    ax = prize[0][0]; ay = prize[0][1]; bx = prize[1][0]; by = prize[1][1]; px = prize[2][0] + offset; py = prize[2][1] + offset
    if (+by*px-bx*py) % (ax*by - ay*bx) == 0 and (-ay*px+ax*py) % (ax*by - ay*bx) == 0:
        return ((+by*px-bx*py) // (ax*by - ay*bx), (-ay*px+ax*py) // (ax*by - ay*bx))
    else: 
        return (0,0)

# advent of code 2024 day 13
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        
        self.parsed = []
        tmp = []
        for line in  self.data.splitlines():
            if line == '':
                self.parsed.append(tmp)
                tmp = []
            else: 
                tmp0 = tuple(int(match) for match in re.findall(pattern0, line))
                tmp.append(tmp0)  
        self.parsed.append(tmp)         

    def part_one(self, **kwargs):
        prizes = self.parsed
        self.part_one_result = sum([3*a+b for a,b in map(lambda x: find_tokens(x, 0),prizes)])

    def part_two(self, **kwargs):
        prizes = self.parsed
        self.part_two_result = sum([3*a+b for a,b in map(lambda x: find_tokens(x, 10000000000000),prizes)])
