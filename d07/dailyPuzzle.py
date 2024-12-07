from dxx.superDailyPuzzle import SuperDailyPuzzle

from collections import namedtuple
import itertools

Equation = namedtuple('Equation', ['result', 'operands'])

OPERATOR_MAP1 = {0: lambda a,b: a+b, 1: lambda a,b: a*b}
OPERATOR_MAP2 = {0: lambda a,b: a+b, 1: lambda a,b: a*b, 2:lambda a,b: int(str(a)+str(b))}

# advent of code 2023 day 7 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [Equation(result= int(line.split(":")[0]), operands= [int(num) for num in (line.split(":")[1]).split()]) for line in self.data.splitlines()]

    def part_one(self, **kwargs):
        res1 = 0
        for equation in self.parsed:
            for operators in itertools.product([0, 1], repeat=len(equation.operands)-1):
                tmp = equation.operands[0]
                for idx, operator in enumerate(operators): tmp = OPERATOR_MAP1[operator](tmp, equation.operands[idx+1])
                if tmp == equation.result: res1 += equation.result; break

        self.part_one_result = res1

    def part_two(self, **kwargs):
        res2 = 0
        for equation in self.parsed:
            for operators in itertools.product([0, 1, 2], repeat=len(equation.operands)-1):
                tmp = equation.operands[0]
                for idx, operator in enumerate(operators): tmp = OPERATOR_MAP2[operator](tmp, equation.operands[idx+1])
                if tmp == equation.result: res2 += equation.result; break

        self.part_two_result = res2