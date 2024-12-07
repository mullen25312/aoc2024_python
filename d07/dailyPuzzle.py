from dxx.superDailyPuzzle import SuperDailyPuzzle

from collections import namedtuple
import itertools

Equation = namedtuple('Equation', ['result', 'operands'])
OPERATOR_MAP = [lambda a,b: a+b, lambda a,b: a*b, lambda a,b: int(str(a)+str(b))]

def check_equation(equation, number):
    for operators in itertools.product(range(number), repeat=len(equation.operands)-1):
        tmp = equation.operands[0]
        for idx, operator in enumerate(operators): tmp = OPERATOR_MAP[operator](tmp, equation.operands[idx+1])
        if tmp == equation.result: return equation.result
    return 0

# advent of code 2023 day 7 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [Equation(result= int(line.split(":")[0]), operands= [int(num) for num in (line.split(":")[1]).split()]) for line in self.data.splitlines()]

    def part_one(self, **kwargs):
        self.part_one_result = sum([check_equation(equation, 2) for equation in self.parsed])

    def part_two(self, **kwargs):
        self.part_two_result = sum([check_equation(equation, 3) for equation in self.parsed])