class SuperDailyPuzzle:
    data: None
    parsed: None
    part_one_result: None
    part_two_result: None

    def __init__(self, data_path):
        with open(data_path, "r") as file:
            self.data = file.read()

    def parse(self, **kwargs):
        self.parsed = None

    def part_one(self, **kwargs):
        self.part_one_result = None

    def part_two(self, **kwargs):
        self.part_two_result = None
