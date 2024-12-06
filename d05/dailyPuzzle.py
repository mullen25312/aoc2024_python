from dxx.superDailyPuzzle import SuperDailyPuzzle

def check_correctness(update, rules):
    for idx, num1 in enumerate(update):
        if num1 not in rules: continue
        for num2 in rules[num1]:
            if num2 in update:
                if idx > update.index(num2): 
                    return [idx, update.index(num2)]
    return True


# advent of code 2023 day 5 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        rules = {}
        for line in self.data.split("\n\n")[0].splitlines():
            if int(line.split("|")[0]) in rules: rules[int(line.split("|")[0])].append(int(line.split("|")[1]))
            else: rules[int(line.split("|")[0])] = [int(line.split("|")[1])]

        updates = [[int(num) for num in line.split(",")] for line in self.data.split("\n\n")[1].splitlines()]
        self.parsed = [rules, updates]

    def part_one(self, **kwargs):
        [rules, updates] = self.parsed
        self.part_one_result = sum([(check_correctness(update, rules)==True)*update[len(update)//2] for update in updates])

    def part_two(self, **kwargs):
        [rules, updates] = self.parsed

        res2 = 0
        for update in updates:
            if check_correctness(update, rules) == True: continue
            else:
                while check_correctness(update, rules) != True:
                    [num1, num2] = check_correctness(update, rules)
                    update[num1], update[num2] = update[num2], update[num1]
                res2 += update[len(update)//2]

        self.part_two_result = res2